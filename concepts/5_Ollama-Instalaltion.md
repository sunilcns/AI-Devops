Lama Models key links :

1. https://ollama.com/library/llama3.2

2. https://medium.com/pythoneers/llama-3-2-1b-and-3b-small-but-mighty-23648ca7a431
--------------------------------------------------------------------------------------------------------------------------------
To check Olama is running :
curl http://localhost:11434
 -> Ollama is running


# Ollama server - runs automatically (no need to start)

# Only run this when you want to CHAT interactively
ollama run llama3.2

# Only run this when you want a QUICK one-shot answer
ollama run llama3.2 "What is Docker?"

# Only run this if server stopped for some reason
ollama serve






Errors : 
Once Ollama is installed by default it may start working in any language. 
for me it was :
"Soy aquí para ayudar. ¿Hay algo en particular que quieras hablar o necesitas información sobre algún tem"
It is a spanish. Just to restart the bash .

We can use llama3.2:1b which uses 1b trained parameters 


 1.  ollama -h -> To help 
 2.  ollama run llama3.2:1b
    Starts the model and opens chat

    C:\Users\sunil>ollama run llama3.2:1b
        >>> hello llm
        Hello! How can I assist you today?

  3. ollama list
        C:\Users\sunil>ollama list
        NAME           ID              SIZE      MODIFIED
        llama3.2:1b    baf6a787fdff    1.3 GB    10 minutes ago
        C:\Users\sunil>

  4. ollama pull llama3.2:1b
      Downloads model without running

  5. ollama rm llama3.2:1b
     Deletes model to free space

  6. ollama show llama3.2:1b

          Displays details like size, parameters
        
          C:\Users\sunil>ollama show llama3.2:1b
              Model
                architecture        llama
                parameters          1.2B
                context length      131072
                embedding length    2048
                quantization        Q8_0
            
              Capabilities
                completion
                tools
            
              License
                LLAMA 3.2 COMMUNITY LICENSE AGREEMENT
                Llama 3.2 Version Release Date: September 25, 2024
                ...
   7. ollama serve
      Starts local API server

ollama pull = Install software
ollama run = Open software
ollama list -> Always execute this to make sure you are running with defined llama version 
C:\Users\sunil>ollama list
NAME           ID              SIZE      MODIFIED
llama3.2:1b    baf6a787fdff    1.3 GB    About an hour ago

C:\Users\sunil>
      
  -----------------------------------------------------------------------------------------------------------------------
  Usage :
  1. # Quick Q&A / Chat
      bash# Ask anything directly
      ollama run llama3 "What is DevOps?"
      ollama run llama3 "Explain microservices in simple terms"
      ollama run llama3 "Difference between Docker and Kubernetes"

  2. # Code Generation
      bash# Generate scripts
      ollama run codellama "Write a Python script to monitor CPU usage"
      ollama run codellama "Write a bash script to backup files"
      ollama run codellama "Write a Dockerfile for a Node.js app"

      -Fix code
      ollama run codellama "Fix this Python code: def add(a,b) return a+b"

      - Explain code
      ollama run codellama "Explain this code: $(cat myscript.py)"

  3. # Log Analysis
      bash# Analyze logs directly
      ollama run llama3 "Analyze this log and find errors: $(cat app.log)"

      Find root cause
      ollama run llama3 "What is the root cause of this error:
      ConnectionRefusedError: [Errno 111] Connection refused"

      Summarize logs
      ollama run llama3 "Summarize this log file: $(tail -50 /var/log/syslog)"

  4. # Write & Review IaC (Terraform / Kubernetes)
      bash# Generate Terraform
      ollama run codellama "Write Terraform code to create AWS S3 bucket"

      - Review Terraform plan
      ollama run llama3 "Review this Terraform plan and suggest improvements:
      $(cat plan.tf)"
      - Generate Kubernetes YAML
      ollama run codellama "Write Kubernetes deployment YAML for nginx with 3 replicas"
      - Debug Kubernetes
      ollama run llama3 "Fix this Kubernetes YAML: $(cat deployment.yaml)"

5. # Write Documentation
    bash# Generate README
    ollama run llama3 "Write a README.md for a Python Flask REST API project"
    - Document a script
    ollama run llama3 "Write documentation for this script: $(cat deploy.sh)"
    - Write runbook
    ollama run llama3 "Write a runbook for deploying a Node.js app to AWS EC2"

6. Security Review
    bash# Review script for security issues
    ollama run llama3 "Review this script for security vulnerabilities: $(cat script.sh)"
    - Check Dockerfile security
    ollama run llama3 "Find security issues in this Dockerfile: $(cat Dockerfile)"
    - Suggest best practices
    ollama run llama3 "What are security best practices for AWS IAM roles?"

7. # Debugging & Troubleshooting
    bash# Debug errors
    ollama run llama3 "How to fix: Error response from daemon: port is already allocated"

    - Kubernetes issues
    ollama run llama3 "How to fix Kubernetes CrashLoopBackOff error"

    - Jenkins issues
    ollama run llama3 "Jenkins pipeline failed with exit code 1, how to debug?"

8.  # Generate Test Data
    bash# Generate sample JSON
    ollama run llama3 "Generate 5 sample JSON records for a user database"
    - Generate test cases
    ollama run codellama "Write unit tests for this Python function: $(cat utils.py)"
    - Generate dummy data
    ollama run llama3 "Generate sample CSV data with name, email, age columns"

9.  # CI/CD Pipeline Help
    bash# Generate GitHub Actions
    ollama run codellama "Write GitHub Actions workflow for Python app CI/CD"
    - Generate Jenkinsfile
    ollama run codellama "Write a Jenkinsfile for building and deploying a Docker image"
    - Optimize pipeline
    ollama run llama3 "How can I optimize this CI/CD pipeline: $(cat Jenkinsfile)"

10. # API Usage in Scripts
    bash# Use Ollama API in shell script
    #!/bin/bash
    QUESTION="How to reduce Docker image size?"

    curl -s http://localhost:11434/api/generate \
      -d "{
        \"model\": \"llama3\",
        \"prompt\": \"$QUESTION\",
        \"stream\": false
      }" | jq '.response'
 

