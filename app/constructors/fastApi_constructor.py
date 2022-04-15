import os
from ..configs.defaults import root_path
from .defaults.paths import fast_api, version

def exists_defaults():
    if os.path.isdir(os.path.join(root_path, "app", "api")):
        return True

    return False


def generate_default():
    fast_api.generate_path()


def generate_new_version_structure(version_name):
    if not exists_defaults():
        generate_default()
    version.generate_path(version_name)


def generate_new_model_structure():
    pass
