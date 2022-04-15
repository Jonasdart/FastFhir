import os
import subprocess
from ..files import generate_init_file, generate_api_file, generate_main_file
from ....configs.defaults import root_path


def generate_path():
    initial_path = os.path.join(root_path, "app")

    os.makedirs(initial_path)
    generate_init_file(initial_path)

    api_path = os.path.join(initial_path, "api")
    os.makedirs(api_path)
    generate_init_file(api_path)

    tests_path = os.path.join(initial_path, "tests")
    os.makedirs(tests_path)
    generate_init_file(tests_path)

    utils_path = os.path.join(initial_path, "utils")
    os.makedirs(utils_path)
    generate_init_file(utils_path)
