import json
from .db_manager import database, Query

def get_versions():
    table_versions = database.table("versions")
    return table_versions.all()

def get_version(version_name):
    table_versions = database.table("versions")
    version_orm = Query()

    version = table_versions.search((version_orm.name == version_name))

    return version

def save_new_version(version):
    if get_version(version["name"]):
        raise AssertionError("This version already exists!")

    table_versions = database.table("versions")
    table_versions.insert(version)

    return True