import os

from config import MAX_CHARS
from functions.get_files_info import PathException


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        absolute_path: str = os.path.abspath(working_directory)
        full_file_path: str = os.path.normpath(os.path.join(absolute_path, file_path))

        if os.path.commonpath((absolute_path, full_file_path)) != absolute_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(full_file_path):
            return f'Error: File not found or is not a regular file: "{full_file_path}"'
        with open(full_file_path, "r") as f:
            content_string = f.read(MAX_CHARS)
            if f.read(1):
                content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return content_string
    except PathException as e:
        return f"Error: {e}"
