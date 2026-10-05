import os


class PathException(Exception):
    def __init__(self, *args) -> None:
        super().__init__(*args)

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        absolute_path: str = os.path.abspath(working_directory)
        full_path: str = os.path.normpath(os.path.join(absolute_path, directory))

        if os.path.commonpath((absolute_path, full_path)) != absolute_path:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'

        files: list[str] = os.listdir(full_path)
        files_metadata: list[str] = []
        for file in files:
            file_size = os.path.getsize(full_path + f"/{file}")
            is_dir = os.path.isdir(full_path + f"/{file}")
            meta_str = f"- {file}: file_size={file_size}, is_dir={is_dir}"
            files_metadata.append(meta_str)
        dir_content: str = "\n".join(files_metadata)
        return f'Success: "{directory}" is within the working directory' + f"\n{dir_content}"
    except PathException as e:
        return f"Error: {e}"
