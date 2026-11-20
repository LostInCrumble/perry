import os

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Get the info for all the files and directories in a given directory",
        "parameters": {
            "type": "object",
            "required": ["dir"],
            "properties": {
                "dir": {
                    "type": "string",
                    "description": "The name of the directory to get all the files informations",
                }
            },
        },
    },
}


def get_files_info(working_dir: str, dir: str = ".") -> str:
    working_dir_abs_path = os.path.abspath(working_dir)
    target_path = os.path.normpath(os.path.join(working_dir_abs_path, dir))

    if not os.path.isdir(target_path):
        return f"Error: cannot list {dir} content as it is not a directory"

    res = []
    for item in os.listdir(target_path):
        item_abs_path = os.path.normpath(os.path.join(target_path, item))
        res.append(
            f"- {item_abs_path}: size={os.path.getsize(item_abs_path)} bytes, is_dir={os.path.isdir(item_abs_path)}"
        )

    return "".join(res)
