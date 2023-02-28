from invoke import task
from pathlib import Path
import sys
import shutil

sys.path.append(f"{Path(__file__).parent.parent.resolve()}/core-build-py")
sys.path.append(f"{Path(__file__).resolve().parent}")
import eot.build.bootstrap
import eot.build.tasks


ns = eot.build.tasks.load()

this_dir = Path(__file__).parent


def repo_version():
    from eot.build.deploy import get_version

    return get_version(this_dir)


@task()
def build(context):
    """
    Build the library
    """
    with context.cd(str(this_dir)):
        context.run("python -m build")


ns.add_task(build)

@task()
def clean(context):
    """
    Clean the build
    """
    with context.cd(this_dir):
        print(f"{this_dir = }")
        shutil.rmtree(this_dir / "dist", ignore_errors=True)
        shutil.rmtree(this_dir / "build", ignore_errors=True)
        shutil.rmtree(this_dir / "var", ignore_errors=True)

        for folder in this_dir.glob("*.egg-info"):
            shutil.rmtree(folder, ignore_errors=True)

        shutil.rmtree(this_dir / "var", ignore_errors=True)


ns.add_task(clean)


@task()
def deploy(context, build="wheel"):
    """
    Deploy eot-wowool-sdk Python package to Nexus build types are ['wheel' , 'source']
    """
    from eot.build.deploy import upload_dist_folder

    upload_dist_folder(context, this_dir, "wow*test*project")

ns.add_task(deploy)

