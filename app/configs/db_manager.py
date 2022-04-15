from tinydb import TinyDB, Query
from .defaults import root_path, VERSIONS_PATHS
import os


database = TinyDB(
    os.path.join(root_path, VERSIONS_PATHS, ".config.json"),
)
