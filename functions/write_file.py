import os

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Write some text to a given file",
        "parameters": {
            "type": "object",
            "required": ["file_name", "content"],
            "properties": {
                "file_name": {
                    "type": "string",
                    "description": "The name of the file to write to",
                },
                "content": {
                    "type": "string",
                    "description": "The content to write in the given file",
                },
            },
        },
    },
}


def write_file(working_dir: str, file_name: str, content: str) -> str:
    working_dir_abs_path = os.path.abspath(working_dir)
    target_file = os.path.normpath(os.path.join(working_dir_abs_path, file_name))

    if os.path.isdir(target_file):
        return f"Error: cannot write into {file_name} as it is a directory"

    try:
        with open(target_file, "w") as f:
            f.write(content)
        return f"Successfully wrote into {file_name}"
    except FileNotFoundError:
        return f"Error: {file_name} does not exist"
    except PermissionError:
        return f"Error: do not have the access rights to write to {file_name}"
    except OSError:
        return "Error: an unknown error occurred"
