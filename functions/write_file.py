import os

from functions.get_files_info import PathException


def write_file(
    working_directory: str,
    file_path: str,
    content: str
) -> str:
    try:
        absolute_path: str = os.path.abspath(working_directory)
        full_file_path: str = os.path.normpath(os.path.join(absolute_path, file_path))

        if os.path.commonpath((absolute_path, full_file_path)) != absolute_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(full_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        # Checking if all parent directories of the file exist - if so, this will do nothing
        os.makedirs(absolute_path, exist_ok=True)

        with open(full_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except PathException as e:
        return f"Error: {e}"
