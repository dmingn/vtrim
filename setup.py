# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = {"": "src"}

packages = ["vtrim"]

package_data = {"": ["*"]}

install_requires = ["click>=8.0.1,<9.0.0", "ffmpeg-python>=0.2.0,<0.3.0"]

entry_points = {"console_scripts": ["vtrim = vtrim.vtrim:main"]}

setup_kwargs = {
    "name": "vtrim",
    "version": "1.0.0",
    "description": "",
    "long_description": None,
    "author": "dmingn",
    "author_email": "dmingn@users.noreply.github.com",
    "maintainer": None,
    "maintainer_email": None,
    "url": None,
    "package_dir": package_dir,
    "packages": packages,
    "package_data": package_data,
    "install_requires": install_requires,
    "entry_points": entry_points,
    "python_requires": ">=3.9,<4.0",
}


setup(**setup_kwargs)
