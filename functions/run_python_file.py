import os
import subprocess

from functions.get_files_info import PathException


def run_python_file(
    working_directory: str,
    file_path: str,
    args: list[str] | None = None
) -> str:
    try:
        absolute_path: str = os.path.abspath(working_directory)
        full_file_path: str = os.path.normpath(os.path.join(absolute_path, file_path))

        if os.path.commonpath((absolute_path, full_file_path)) != absolute_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(full_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not full_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        #Building a command to run for the agent - extending command list if args are present
        command: list[str] = ["python", full_file_path]
        if args:
            command.extend(args)
        command_process = subprocess.run(
            command, capture_output=True, text=True, timeout=30,
        )
        if command_process.returncode != 0:
            return f'Process exited with code {command_process.returncode}'
        if command_process.stderr and command_process.stdout == "":
            return "No output produced"
        else:
            return f"STDOUT: {command_process.stdout}\nSTDERR: {command_process.stderr}"
    except PathException as e:
        return f"Error: {e}"
