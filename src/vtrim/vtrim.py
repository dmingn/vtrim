import os
from pathlib import Path

import click
import docker
import ffmpeg


@click.command()
@click.argument(
    "input_file",
    type=click.Path(exists=True, dir_okay=False, resolve_path=True, path_type=Path),
)
@click.option("--ss", type=str, default=None)
@click.option("--to", type=str, default=None)
@click.option("--transcode/--no-transcode", default=True)
def vtrim(input_file: Path, ss: str, to: str, transcode: bool):
    working_dir = input_file.parent
    output_file = input_file.with_stem("_".join([input_file.stem, ss, to]))

    if transcode:
        command = (
            ffmpeg.input(str(input_file), ss=ss, to=to)
            .output(str(output_file))
            .get_args()
        )
    else:
        command = (
            ffmpeg.input(str(input_file))
            .output(str(output_file), codec="copy", ss=ss, to=to)
            .get_args()
        )

    docker.from_env().containers.run(
        image="jrottenberg/ffmpeg:4.4-alpine38",
        command=command,
        user=f"{os.getuid()}:{os.getgid()}",
        volumes={
            "/etc/passwd": {"bind": "/etc/passwd", "mode": "ro"},
            "/etc/group": {"bind": "/etc/group", "mode": "ro"},
            str(working_dir): {"bind": str(working_dir), "mode": "rw"},
        },
        working_dir=str(working_dir),
    )


def main():
    vtrim()


if __name__ == "__main__":
    main()
