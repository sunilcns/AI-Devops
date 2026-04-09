import ollama
print ("INSIDE SCRIPT ")
PROMPT = """
Generate a minimal working project for {language} using {framework}.

Output in this EXACT format:

--- Dockerfile ---
<dockerfile content>

--- docker-compose.yml ---
<compose content>

--- app code ---
<code content>

Rules:
- Production-ready but simple
- Use best practices
- No explanations
"""


def generate_project_func(language, framework):
    response = ollama.chat(
        model="llama3.2:1b",
        messages=[
            {
                "role": "system",
                "content": "You are a senior DevOps engineer and backend developer."
            },
            {
                "role": "user",
                "content": PROMPT.format(language=language, framework=framework)
            }
        ]
    )
    
    return response["message"]["content"]


def main():
    print("=== generate_project Generator (powered by Ollama llama3.2) ===\n")
    language = input("Enter the programming language (e.g. python, java, node): ").strip()
    framework = input("Enter the framework (e.g. python, java, node): ").strip()
    print(f"\n Generating Dockerfile for '{language}' and '{language}'....")
    generate_project = generate_project_func(language, framework)
    print("\n--- Generated Dockerfile ---")
    print(generate_project)
    print("----------------------------\n")

if __name__ == "__main__":
    main()    