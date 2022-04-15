import os
from unittest import mock
from app.constructors import version_generator
from app.configs import version_manager


def test_001_get_versions_in_path():
    assert version_generator.get_versions_in_path()


def test_002_save_and_search_new_version_in_db():
    version = {"name": "v1", "path": "./test"}

    assert version_manager.save_new_version(version)
    assert version in version_manager.get_version(version["name"])


def test_003_general_scope():
    assert version_generator.create_version()
