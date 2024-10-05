# LL_model class

## generate method


**Description:** Generate a response for a given prompt with a provided model. 

**Parameters:**

- **model**(str, optional): the model name.(By default =llama3)
- **prompt**(str, required): the prompt to generate a response for.
- **system_message**(str, optional): system message (this will override what is written in the `Modelfile`).
- **output_file**(str, optinal): The output file can be pdf,json or txt.
- **options**(dict, optional): additional model parameters available in the documentation of the modelfile.
- **template**(str, optional): the prompt template to use (overrides what is defined in the `Modelfile`)

**Examples**

~~~python
response = LL_model.generate( 
    prompt='Tell me a joke.',
    output_file='joke_output.txt'
)
print(response)
~~~

~~~python
response = LL_model.generate(
    model="llama3.1",
    prompt='How can I learn Data Science?',
    output_file="DS.json",
    options={
        "temperature":0.6
    }
)
print(response)
~~~
