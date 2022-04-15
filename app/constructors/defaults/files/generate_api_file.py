import os


def generate_api_file(initial_path):
    file_name = "api.py"

    path_of_destiny_file = os.path.join(initial_path, file_name)
    path_of_base_file = os.path.join(__file__, "version_api_file")

    os.system(f'cat "{path_of_base_file}" > "{path_of_destiny_file}"')
