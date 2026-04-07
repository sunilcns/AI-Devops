Lama Models key links :
https://ollama.com/library/llama3.2
https://medium.com/pythoneers/llama-3-2-1b-and-3b-small-but-mighty-23648ca7a431

Errors : 
Once Ollama is installed by default it may start working in any language. 
for me it was :
"Soy aquí para ayudar. ¿Hay algo en particular que quieras hablar o necesitas información sobre algún tem"
It is a spanish. Just to restart the bash .

We can use llama3.2:1b which uses 1b trained parameters 


ollama -h -> To help 
ollama run llama3.2:1b
Starts the model and opens chat

ollama list
    C:\Users\sunil>ollama list
    NAME           ID              SIZE      MODIFIED
    llama3.2:1b    baf6a787fdff    1.3 GB    10 minutes ago
    C:\Users\sunil>

ollama pull llama3.2:1b
Downloads model without running

ollama rm llama3.2:1b
Deletes model to free space


