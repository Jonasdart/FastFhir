import os
from . import root_path
from ..configs.defaults import VERSIONS_PATHS
from ..configs import version_manager
from . import fastApi_constructor


def generate_version(version):
    new_version = {"name": version["versionName"], "path": version["versionPath"]}

    return new_version


def persist_version(version):
    version_manager.save_new_version(version)

    return True


def verify_if_exists_a_new_version(versions):
    for version in versions:
        if not version_manager.get_version(version):
            return version


def get_versions_in_path():
    versions_path = os.path.join(root_path, VERSIONS_PATHS)
    versions = []
    if os.path.isdir(versions_path):
        for version in os.listdir(versions_path):
            path = os.path.abspath(os.path.join(versions_path, version))
            if os.path.isdir(path):
                versions.append(
                    {
                        "versionName": version,
                        "versionPath": path,
                    }
                )
    if versions: return versions
    raise FileNotFoundError("The versions path does not exists into interfaces path")


def create_version():
    versions = get_versions_in_path()

    new_version = verify_if_exists_a_new_version(versions)
    if new_version:
        version = generate_version(new_version)
        if persist_version(version):
            generate_fastAPI_version(version)

    return True


def generate_fastAPI_version(version):
    fastApi_constructor.generate_new_version_structure(version["name"])
