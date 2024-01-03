from invoke import task
from pathlib import Path
from subprocess import run


this_dir = Path(__file__).parent


# def repo_version():
#     from eot.build.deploy import get_version

#     return get_version(this_dir)


@task()
def build(context):
    """
    Build the library
    """
    # run("python -m build" , cwd=str(this_dir), check=True, shell=True)
    context.run("python3 -m build")


@task()
def clean(context):
    """
    Clean the build
    """
    import shutil

    with context.cd(this_dir):
        print(f"{this_dir = }")
        shutil.rmtree(this_dir / "dist", ignore_errors=True)
        shutil.rmtree(this_dir / "build", ignore_errors=True)
        shutil.rmtree(this_dir / "var", ignore_errors=True)

        for folder in this_dir.glob("*.egg-info"):
            shutil.rmtree(folder, ignore_errors=True)

        shutil.rmtree(this_dir / "var", ignore_errors=True)


@task
def version(_):
    from eot.build.git import get_version
    from pathlib import Path

    version_eot = get_version(Path(__file__).parent)
    print(f"==core-build=+ 6===>>>>>>>>{version_eot=}")

    from setuptools_scm import get_version as get_version_scm

    version_scm = get_version_scm(Path(__file__).parent)
    print(f"===version_scm + 6===>>>>>>>>{version_scm=}")
