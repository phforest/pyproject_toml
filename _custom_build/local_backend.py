from setuptools import build_meta as _orig
from setuptools.build_meta import *
from packaging.version import Version

# from eot.build.git import get_version
from pathlib import Path
from setuptools_scm import get_version

__version__ = get_version()

# __version__ = get_version(Path(__file__).parent.parent)


def get_requires_for_build_wheel(config_settings=None):
    return _orig.get_requires_for_build_wheel(config_settings)


# + ["rich"]


def get_requires_for_build_sdist(config_settings=None):
    return _orig.get_requires_for_build_sdist(config_settings)


def prepare_metadata_for_build_editable(self, metadata_directory, config_settings=None):
    print("========>>>>>metadata_directory", metadata_directory, config_settings)
