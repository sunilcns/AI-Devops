

<img width="846" height="487" alt="image" src="https://github.com/user-attachments/assets/aaeb2807-7c1b-4977-871d-09c723e59ab8" />


This project demonstrates how to integrate a local Large Language Model (LLM) into a Python script to automate a real development task. The user provides a programming language as input (e.g. `python`, `java`, `node`), and the script uses Ollama's `llama3.2` model to generate a production-ready `Dockerfile` tailored to that language, which is then saved to disk.

The entire workflow runs locally — no internet or cloud API keys required.


## Software & Tools Required

| Tool / Software | Version | Purpose |
|---|---|---|
| **Python** | 3.8 or higher | Runtime for the script |
| **pip** | Latest | Python package manager |
| **Ollama** | Latest | Local LLM runtime |
| **llama3.2** (via Ollama) | Latest | The language model used for generation |
| **ollama** (Python library) | Latest | Python client to communicate with Ollama |
| **venv** (built-in) | — | Python virtual environment manager |


## Key Concepts

| Concept | Summary |
|---|---|
| **Local LLM inference** | Ollama runs the `llama3.2` model entirely on your machine — no data leaves your system and no API key is needed. |
| **`ollama.chat()`** | The Python client method that sends a structured message list (system prompt + user prompt) to the model and returns the generated response, mirroring the chat completion pattern used by cloud LLM APIs. |
| **System prompt engineering** | A `system` role message instructs the model to return only raw Dockerfile content, keeping the output clean and directly writable to disk without post-processing. |
| **Python virtual environment** | Isolates project dependencies from your global Python installation, preventing version conflicts across projects. |
| **Prompt-to-file pipeline** | The core pattern — accept user input → construct a prompt → call the LLM → parse the response → write output to disk — is reusable for any text generation automation task. |
