import os


def generate_main_file(initial_path):
    file_name = "main.py"

    path_of_destiny_file = os.path.join(initial_path, file_name)
    path_of_base_file = os.path.join(__file__, "main_file")

    os.system(f'cat "{path_of_base_file}" > "{path_of_destiny_file}"')
