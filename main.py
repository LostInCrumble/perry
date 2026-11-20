import os
import sys

from dotenv import load_dotenv
from ollama import ChatResponse, ResponseError, chat

from functions.get_file_content import get_file_content, schema_get_file_content
from functions.get_files_info import get_files_info, schema_get_files_info
from functions.run_python_file import run_python_file, schema_run_python_file
from functions.write_file import schema_write_file, write_file
from terminal import *

available_functions = {
    "get_file_content": get_file_content,
    "get_files_info": get_files_info,
    "run_python_file": run_python_file,
    "write_file": write_file,
}

tools = [
    schema_get_file_content,
    schema_get_files_info,
    schema_run_python_file,
    schema_write_file,
]


def main():
    clear_screen()
    go_to_home_position()
    print_title()

    load_dotenv()

    try:
        model = os.environ["MODEL"]
    except KeyError:
        print(get_error_text('Error: "MODEL" environment variable is not set properly'))
        sys.exit()

    print(f"Model: {model}")

    messages = []
    while True:
        prompt = input("You > ")
        messages.append({"role": "user", "content": prompt})

        try:
            response: ChatResponse = chat(model=model, messages=messages, tools=tools)
        except ResponseError as e:
            print(get_error_text(str(e)))
            sys.exit()

        if response.message.tool_calls:
            messages.append(response.message)

            for tool in response.message.tool_calls:
                if function_to_call := available_functions.get(tool.function.name):
                    print(f"Calling function {function_to_call}")
                    output = function_to_call(os.getcwd(), **tool.function.arguments)
                else:
                    print(f"Function {function_to_call} not found")
                    output = "Function not found"

                messages.append(
                    {
                        "role": "tool",
                        "content": str(output),
                        "tool_name": tool.function.name,
                    }
                )

        final_response = chat(model=model, messages=messages, stream=True)
        print("Perry > ", end="", flush=True)
        for chunk in final_response:
            print(chunk["message"]["content"], end="", flush=True)
        print("\n", end="")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye!")
