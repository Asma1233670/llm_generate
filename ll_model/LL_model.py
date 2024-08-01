from ._config import  Create_client, DEFAULT_MODEL_NAME
import ollama
import json, os
from .OutputHandler import OutputHandler

class LL_model:
    #client=Create_client()
    model_name=DEFAULT_MODEL_NAME

    @classmethod
    def create(self, model_name, modelfile=None, modelfilepath=None):
        if modelfile:
            print(f"Creating model '{model_name}' with modelfile.")
            ollama.create(model=model_name, modelfile=modelfile)
        elif modelfilepath:
            print(f"Creating model '{model_name}' with modelfile path: {modelfilepath}.")
            if os.path.exists(modelfilepath):
                ollama.create(model=model_name, path=modelfilepath)
            else:
                raise FileNotFoundError(f"The specified model file path does not exist: {modelfilepath}")
        else:
            raise ValueError("You must provide either a model file or the path to a model file.")
        self.model_name = model_name
        
    #The difference between ollama.chat and ollama.generate: 
    #-ollama.chat: maintains conversation context across multiple interactions.
    #-ollama.generate: does not maintain any context and treats each prompt independently.
    @classmethod
    def generate(self,model=model_name ,prompt='', system_message=None, output_file=None):
        generate_args = {
           'model': model,
           'prompt': prompt
        }
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
            output = ollama.generate(**generate_args,stream=False)
            response_text = output['response']
            if output_format == 'json' and output_file:
                with open(output_file, 'w') as f:
                    json.dump(response_text, f, indent=4)
            elif output_format and output_format != 'json':
                OutputHandler(response_text, output_format, output_file)
            return response_text
        except Exception as e:
            print(f"An error occurred during generation: {e}")
            return None
    @classmethod
    def chat(self,model=model_name ,prompt='',system_message=None,output_file=None):
        messages=[]
        if system_message:
            messages.append({"role":"system","content":system_message})
        if prompt:
            messages.append({"role":"user","content":prompt})
        try:
            response=ollama.chat(model,messages)
            response_txt=response['message']['content']
            conversation = {
                'user_message': prompt,
                'assistant_message': response_txt
            }
            output_format=None
            if output_file:
                _, file_extension=os.path.splitext(output_file)
                if file_extension:
                    output_format= file_extension.lstrip('.').lower()
            if output_format == 'json' and output_file:
                with open(output_file,'w',encoding='utf-8') as f:
                    json.dump(conversation, f, ensure_ascii=False, indent=4)
            elif output_file and output_format!='json':
                OutputHandler(f"User: {prompt}\nAssistant: {response_txt}",output_format,output_file)
            return conversation
        except Exception as e:
            print(f"An error occurred during the chat: {e}")
            return None



    


