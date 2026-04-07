Lama Models key links :

1. https://ollama.com/library/llama3.2

2. https://medium.com/pythoneers/llama-3-2-1b-and-3b-small-but-mighty-23648ca7a431
------------------------------------------------------------------------------------------------------------------------------------------------------
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
      
  
 

