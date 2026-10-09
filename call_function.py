# This file congregates all the function schemas (tools)
# for the LLM to use/"call"

from functions.get_files_info import schema_get_files_info

available_functions = [
    schema_get_files_info,
]
