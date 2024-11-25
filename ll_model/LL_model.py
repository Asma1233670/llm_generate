import sys, json, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from  _config import  Create_client, DEFAULT_MODEL_NAME
from .OutputHandler import OutputHandler

class LL_model:
    client=Create_client()
    model_name=DEFAULT_MODEL_NAME

    @classmethod
    def create(self, model_name, modelfile=None, modelfilepath=None):
        if modelfile:
            print(f"Creating model '{model_name}' with modelfile.")
            self.client.create(model=model_name, modelfile=modelfile)
        elif modelfilepath:
            print(f"Creating model '{model_name}' with modelfile path: {modelfilepath}.")
            if os.path.exists(modelfilepath):
                self.client.create(model=model_name, path=modelfilepath)
            else:
                raise FileNotFoundError(f"The specified model file path does not exist: {modelfilepath}")
        else:
            raise ValueError("You must provide either a model file or the path to a model file.")
        self.model_name = model_name
        
    #The difference between ollama.chat and ollama.generate: 
    #-ollama.chat: maintains conversation context across multiple interactions.
    #-ollama.generate: does not maintain any context and treats each prompt independently.
    @classmethod
    def generate(self,model=model_name ,prompt='', system_message=None, output_file=None,options=None, template=None):
        generate_args = {
           'model': model,
           'prompt': prompt
        }
        if options:
            generate_args['options'] = options
        if template:
            generate_args['template'] = template
        if system_message:
            generate_args['system'] = system_message
        output_format=None
        if output_file:
            _, file_extension=os.path.splitext(output_file)
            if file_extension:
                output_format= file_extension.lstrip('.').lower()
        if output_format == 'json':
            generate_args['format'] = output_format
        try:
            output = self.client.generate(**generate_args,stream=False)
            response_text = output['response']
            if output_format == 'json' and output_file:
                with open(output_file, 'w',encoding="utf-8") as f:
                    json.dump(response_text, f, indent=4)
            elif output_format and output_format != 'json':
                OutputHandler(response_text, output_file)
            return response_text
        except Exception as e:
            print(f"An error occurred during generation: {e}")
            return None
    @classmethod
    def chat(self,model=model_name ,system_message=None,output_file=None,exit_command="exit"):
        messages = []
        if system_message:
            messages.append({"role": "system", "content": system_message})

        conversation_history = []

        while True:
            # Get user input
            prompt = input("\nYou: ")
            # Exit if user types the exit command
            if prompt.lower() == exit_command:
                print("Exiting the chat...")
                break

            # Append user input to messages
            messages.append({"role": "user", "content": prompt})
            try:
                response = self.client.chat(model, messages)
                response_txt = response['message']['content']
                
                # Append assistant's response to the messages
                messages.append({"role": "assistant", "content": response_txt})
                # Print assistant's response
                print(f"Assistant: {response_txt}")

                # Keep track of conversation history
                conversation = {
                    'user_message': prompt,
                    'assistant_message': response_txt
                }
                conversation_history.append(conversation)

            except Exception as e:
                print(f"An error occurred during the chat: {e}")
                break
        # Once the conversation ends, save it to a file if specified
        if output_file:
            output_format = None
            _, file_extension = os.path.splitext(output_file)
            if file_extension:
                output_format = file_extension.lstrip('.').lower()

            if output_format == 'json':
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(conversation_history, f, ensure_ascii=False, indent=4)
            else:
                with open(output_file, 'w', encoding='utf-8') as f:
                    for convo in conversation_history:
                        f.write(f"User: {convo['user_message']}\n")
                        f.write(f"Assistant: {convo['assistant_message']}\n")
                        f.write("\n")
        return conversation_history




    


