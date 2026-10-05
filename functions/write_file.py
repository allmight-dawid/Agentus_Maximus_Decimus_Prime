import os

from functions.get_files_info import PathException

def write_file(
    working_directory: str,
    file_path: str,
    content: str
) -> str:
