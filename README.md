
# LLM_Generate

`LLM_Generate` is a comprehensive Python SDK designed for seamless interaction custom large language models (LLMs), but primarily focuses on leveraging the power of LLama3 for generating AI-driven responses maintaining interactive conversations. With support for multiple output formats like JSON, PDF, and TXT, `LLM_Generate` ensures that the generated data is easy to manage and integrate into different systems.
This SDK can be used to generate data from different llms (available in ollama).

# Features



* **Model Creation:** Create and initialize custom models from a specified model file or the path of the model file.

* **Text Generation:** Generate responses to prompts with or without system messages, supporting output in JSON, PDF and TXT.

* **Interactive Chat:** Engage in conversations while maintaining context, with options to save the conversation in various formats(JSON, PDF, TXT).


# Installation
Before using tha SDK, you need first to install ollama and pull the model that you're going to use.
[link download ollama](https://ollama.com/download)
Pulling the llm to be used:
~~~shell
ollama pull <model-name>
~~~

1. Download the SDK:
First, download the SDK to your local machine. You can do this by cloning the repository or downloading the ZIP file from the repository page.

2. Navigate to the SDK Directory: Change your directory to the location of the downloaded SDK.

3. Run the following command to install the SDK:
~~~sh
pip install -e . 
~~~

# Command Line Interface


The CLI provides commands to create models, generate responses, and chat with the model.

* **Create a model:**

~~~sh
ll_model create --model_name call_center_agent --modelfilepath modelfile.txt
~~~

* **Generating text:**

~~~sh

ll_model generate --model_name call_center_agent --prompt "Can you tell me about the benefits of our smart home gardening kit?" --system_message "You are a knowledgeable and enthusiastic call center agent promoting and selling our latest smart home gardening kits, which help customers grow fresh vegetables and herbs right at home." --output_file gardening_kit_response.json

~~~

* **Chatting with the model:**

~~~sh

ll_model chat --model_name call_center_agent --prompt "I'm interested in making my home more eco-friendly. What products do you recommend?" --system_message "You are a knowledgeable and enthusiastic call center agent promoting and selling eco-friendly products that make homes more sustainable." --output_file eco_friendly_conversation.txt

~~~
# Python API:


You can also use the SDK directly in your Python code.

~~~python 
from way_llm_model.LL_model import LL_model

LL_model.generate(prompt="Give me a document in the domain of sports.",system_message="You're a AI assistant , that will assist me to create different pdfs in different fields to create a dataset that will be used later for other tasks.",output_file="1.pdf")

~~~

---
