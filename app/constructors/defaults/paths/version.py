import os
import subprocess
from ....configs.defaults import root_path
from ..files import generate_init_file

def generate_path(version_name):
    initial_path = os.path.join(root_path, "app", "api", version_name)

    os.makedirs(initial_path)
    generate_init_file(initial_path)

    endpoints_path = os.path.join(initial_path, "endpoints")
    os.makedirs(endpoints_path)
    generate_init_file(endpoints_path)

    models_path = os.path.join(initial_path, "models")
    os.makedirs(models_path)
    generate_init_file(models_path)

    rules_path = os.path.join(initial_path, "rules")
    os.makedirs(rules_path)
    generate_init_file(rules_path)

    utils_path = os.path.join(initial_path, "utils")
    os.makedirs(utils_path)
    generate_init_file(utils_path)

