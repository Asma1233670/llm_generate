from ollama import Client
#if you want to put ollama in a different machine and point to it 
OLLAMA_HOST="http://localhost:11434/"#11434 ollama default port
DEFAULT_MODEL_NAME="llama3"

def Create_client():
    return Client(host=OLLAMA_HOST)
