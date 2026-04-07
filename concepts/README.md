# AI-Devops
Includes all AI related Devops concepts  


AI-Devops/
│
├── README.md                          # Main repo overview
│
├── concepts/                          # Your existing .md files
│   ├── prompt-engineering.md
│   ├── local-vs-hosted-llm.md
│   └── terraform-workflow.md
│
├── scripts/                           # Reusable utility scripts
│   ├── setup/
│   │   ├── install-ollama.sh          # Local LLM setup
│   │   └── install-terraform.sh
│   ├── monitoring/
│   │   ├── check-cpu.sh
│   │   └── check-disk.sh
│   └── utils/
│       └── llm-query.sh               # Generic LLM API call script
│
├── demos/                             # Hands-on demo activities
│   ├── 01-local-llm/
│   │   ├── README.md
│   │   ├── run-ollama.sh
│   │   └── sample-prompts.txt
│   ├── 02-prompt-engineering/
│   │   ├── README.md
│   │   ├── zero-shot.py
│   │   ├── few-shot.py
│   │   └── chain-of-thought.py
│   ├── 03-terraform-demo/
│   │   ├── README.md
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   ├── 04-kubernetes-demo/
│   │   ├── README.md
│   │   ├── deployment.yaml
│   │   └── debug-pod.sh
│   └── 05-cicd-pipeline/
│       ├── README.md
│       └── .github/workflows/
│           └── demo-pipeline.yml
│
├── llm-integrations/                  # AI + DevOps integrations
│   ├── langchain/
│   │   ├── README.md
│   │   └── basic-chain.py
│   ├── ollama-api/
│   │   ├── README.md
│   │   └── query.py
│   └── claude-api/
│       ├── README.md
│       └── query.py
│
└── docs/
    └── contributing.md