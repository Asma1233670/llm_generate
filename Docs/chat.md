# LL_model class

## chat method

**Description:** Engage in a conversation with the model. This method allows for multi-turn interactions by sending a series of messages back and forth between the user and the model.

**Parameters:**

- **model**(str): the model name. (By default = llama3)
- **system_message**(str, optional): system message (this will override what is written in the modelfile).
- **output_file**(str, optional): The output file can be pdf, json, or txt.
- **exit_command**(str, optional): The keyword that the user can type to exit the chat. Defaults to `exit`.

**Returns:**
- **conversation_history**(list of dict):
A list of dictionaries containing the user's messages and the AI assistant's responses. Each dictionary has two keys:
    - **user_message**: The user's message.
    - **assistant_message**: The assistant's message.
**Examples**

~~~python
response = LL_model.chat(
    model="llama3",
    system_message="You're a helpful assistant!",
    output_file='chat_output.txt',
    exit_command="bye"
)
print(response)
~~~
