from pathlib import Path

import click
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
    output_file = input_file.with_stem("_".join([input_file.stem, ss, to]))

    if transcode:
        ffmpeg.input(input_file, ss=ss, to=to).output(str(output_file)).run()
    else:
        ffmpeg.input(input_file).output(
            str(output_file), codec="copy", ss=ss, to=to
        ).run()


def main():
    vtrim()


if __name__ == "__main__":
    main()
