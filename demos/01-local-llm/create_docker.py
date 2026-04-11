import ollama
import os

def generate_dockerfile(language: str) -> str:
    """Call Ollama using ollama.chat() and return the Dockerfile content."""

    prompt = f"""Generate a production-ready Dockerfile for a {language} application.

Requirements:
- Use an official base image
- Set a working directory
- Copy source files
- Install dependencies (use the standard package manager for {language})
- Expose a sensible default port
- Define a CMD to run the app

Return ONLY the raw Dockerfile content — no markdown fences, no explanation."""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a Docker expert. When asked for a Dockerfile, return only the raw file content. "
                    "No markdown, no commentary, no code fences."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    # Extract the text from the response
    return response["message"]["content"].strip()
 

def main():
    print("=== Dockerfile Generator (powered by Ollama llama3.2) ===\n")
    language = input("Enter the programming language (e.g. python, java, node): ").strip()
    print(f"\nGenerating Dockerfile for '{language}'...")
    dockerfile_content = generate_dockerfile(language)
    print("\n--- Generated Dockerfile ---")
    print(dockerfile_content)
    print("----------------------------\n")

if __name__ == "__main__":
    main()
