import os
import subprocess

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Run a given python file as a script",
        "parameters": {
            "type": "object",
            "required": ["file_name"],
            "properties": {
                "file_name": {
                    "type": "string",
                    "description": "The name of the file to run as a script",
                },
                "args": {
                    "type": "list",
                    "description": "A list of arguments to pass to the python interpreter together with the file name",
                },
            },
        },
    },
}


def run_python_file(
    working_dir: str, file_name: str, args: list[str] | None = None
) -> str:
    working_dir_abs_path = os.path.abspath(working_dir)
    target_file = os.path.normpath(os.path.join(working_dir_abs_path, file_name))

    if os.path.isdir(target_file):
        return f"Error: cannot run {file_name} as it is a directory"

    if not target_file.endswith(".py"):
        return f"Error: cannot run {file_name} as it is not a python file"

    command = ["python", target_file]
    if args:
        command.extend(args)

    try:
        process = subprocess.run(command, capture_output=True, timeout=30, check=False)
    except subprocess.TimeoutExpired:
        return f"Error: timeout expired for {' '.join(command)}"

    res = ""
    if process.returncode != 0:
        res = (
            f"Error: {' '.join(command)} exited with a returncode {process.returncode}"
        )
    if process.stdout:
        res = f"STDOUT: {process.stdout}"
    if process.stderr:
        res = f"STDERR: {process.stderr}"
    return res
