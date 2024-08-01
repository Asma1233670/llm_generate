# LL_model class

## chat method

**Description:** Engage in a conversation with the model. This method allows for multi-turn interactions by sending a series of messages back and forth between the user and the model.

**Parameters:**

- **model**(str): the model name. (By default = llama3)
- **messages**(list, required): a list of message dictionaries. Each dictionary should contain 'role' (either 'user' or 'assistant') and 'content' (the message content).
- **system_message**(str, optional): system message (this will override what is written in the modelfile).
- **output_file**(str, optional): The output file can be pdf, json, or txt.

**Examples**

~~~python
conversation = [
    {'role': 'user', 'content': 'Hello, who are you?'},
    {'role': 'assistant', 'content': 'I am an AI created to assist you.'},
    {'role': 'user', 'content': 'Can you tell me a joke?'}
]

response = LL_model.chat(
    messages=conversation,
    output_file='chat_output.txt'
)
print(response)
~~~
