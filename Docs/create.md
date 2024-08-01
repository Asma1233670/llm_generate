# LL_model class

## Create method:


**Description:** Create a new model, from a [modelfile](Docs/modelfile.md).
---

**Parameters:**
- **name**(str): name of the model to create.
- **modelfile**(str,optional): content of the modelfile.
- **path**(str,optional): path to the modelfile.
---

**Examples:**
- Create a new model using the content of a modelfile:

~~~python
    LL_model.create(model_name="mario",modelfile="FROM llama3 \nSYSTEM You are mario from    Super Mario Bros.")
~~~
 
- Create a new model using the path of a modelfile:

~~~python
   LL_model.create(model_name="helpful Assistant",modelfilepath="Tests/modelfile.txt")
~~~


---
For more informations visit: [ollama create-a-model-api](https://github.com/ollama/ollama/blob/main/docs/api.md#create-a-model)