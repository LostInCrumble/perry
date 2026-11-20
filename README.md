# Perry

A small AI coding agent for local models. Made with Python and Ollama.

> [!WARNING]
> Do not use it too much! It doesn't have all the security and safety features that a production AI agent would have. This is for learning purposes only.

## Quick start

Install [Python](https://www.python.org/), [uv](https://docs.astral.sh/uv/), [Ollama](https://ollama.com/), clone the repo, run `uv sync` in the repo directory and finally run `uv run main.py` or run `uv run pyinstaller perry.spec` to obtain a single file executable. Before running the program you should install locally a model with Ollama and create a .env file in the working directory with the key "MODEL" to specify which model to use.
