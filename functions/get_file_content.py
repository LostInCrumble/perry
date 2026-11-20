import os

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Read the content of a given file",
        "parameters": {
            "type": "object",
            "required": ["file_name"],
            "properties": {
                "file_name": {
                    "type": "string",
                    "description": "The name of the file to read the content from",
                }
            },
        },
    },
}


def get_file_content(working_dir: str, file_name: str) -> str:
    working_dir_abs_path = os.path.abspath(working_dir)
    target_file = os.path.normpath(os.path.join(working_dir_abs_path, file_name))

    if os.path.isdir(target_file):
        return f"Error: cannot read from {file_name} as it is a directory"

    MAX_CHARS = 10_000
    try:
        with open(target_file, "r") as f:
            content = f.read(MAX_CHARS)
        with open(target_file, "r") as f:
            if f.read(1) != "":
                content += f" [trucated at {MAX_CHARS} characters]"
    except FileNotFoundError:
        return f"Error: {file_name} does not exist"
    except PermissionError:
        return f"Error: do not have the access rights to read from {file_name}"
    except OSError:
        return "Error: an unknown error occurred"

    return content
