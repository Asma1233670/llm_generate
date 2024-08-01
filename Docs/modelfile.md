# Writing a modelfile

## Note
The modelfile syntax is currently in development.

A model file is the blueprint to create and share models with Ollama.

## Table of Contents
1. [Format](#format)
2. [Example](#example)
3. [Instructions](#instructions)
   - [FROM (Required)](#from-required)
   - [PARAMETER](#parameter)
   - [TEMPLATE](#template)
   - [SYSTEM](#system)
   - [ADAPTER](#adapter)
   - [LICENSE](#license)
   - [MESSAGE](#message)



## Format
The format of the Modelfile:
```
#comment
INSTRUCTION arguments
```
- **FROM (required)** Defines the base model to use.
- **PARAMETER** Sets the parameters for how Ollama will run the model.
- **TEMPLATE** The full prompt template to be sent to the model.
- **SYSTEM** Specifies the system message that will be set in the template.
- **ADAPTOR** Defines the (Q)LoRA adapters to apply to the model.
- **LICENSE** Specifies the legal license.
- **MESSAGE** Specify message history.

## Example
**Basic model file**

```
FROM llama3
# sets the temperature to 1 (higher is more creative, lower is more coherent)
PARAMETER temperature 1
# sets the context window size to 4096, controlling how many tokens the LLM can use as context to generate the next token
PARAMETER num_ctx 4096
# sets a custom system message to specify the behavior of the chat assistant
SYSTEM You are Mario from super mario bros, acting as an assistant.
```

## Instructions
### FROM (required)
The `FROM` instruction defines the base model to use when creating a model.
```
FROM <model name>:<tag>
```
exp:
```
FROM llama3
```
### PARAMETER 
The `PARAMETER` instruction defines a parameter that can be set when the model is run.
```
PARAMETER <parameter> <parametervalue>
```
**Valid Parameters and Values**
- **mirostat**(int) Enable Mirostat sampling for controlling perplexity. (default: 0, 0 = disabled, 1 = Mirostat, 2 = Mirostat 2.0)*
- **mirostat_eta**(float) Influences how quickly the algorithm responds to feedback from the generated text. A lower learning rate will result in slower adjustments, while a higher learning rate will make the algorithm more responsive. (Default: 0.1)
- **mirostat_tau**(float) Controls the balance between coherence and diversity of the output. A lower value will result in more focused and coherent text. (Default: 5.0)
- **num_ctx**(int) Sets the size of the context window used to generate the next token.
(Default: 2048)
- **repeat_last_n**(int) Sets how far back for the model to look back to prevent repetition. (Default: 64, 0 = disabled, -1 = num_ctx)
- **repeat_penalty**(float) Sets how strongly to penalize repetitions. A higher value (e.g., 1.5) will penalize repetitions more strongly, while a lower value (e.g., 0.9) will be more lenient. (Default: 1.1)
- **temperature**(float) The temperature of the model. Increasing the temperature will make the model answer more creatively. (Default: 0.8)
- **seed**(int) Sets the random number seed to use for generation. Setting this to a specific number will make the model generate the same text for the same prompt. (Default: 0)
- **stop**(string) Sets the stop sequences to use. When this pattern is encountered the LLM will stop generating text and return. Multiple stop patterns may be set by specifying multiple separate `stop` parameters in a modelfile.
- **tfs_z**(float) Tail free sampling is used to reduce the impact of less probable tokens from the output. A higher value (e.g., 2.0) will reduce the impact more, while a value of 1.0 disables this setting. (default: 1)
- **num_predict**(int) Maximum number of tokens to predict when generating text. (Default: 128, -1 = infinite generation, -2 = fill context)
- **top_k**(int) Reduces the probability of generating nonsense. A higher value (e.g. 100) will give more diverse answers, while a lower value (e.g. 10) will be more conservative. (Default: 40)
- **top_p**(float) Works together with top-k. A higher value (e.g., 0.95) will lead to more diverse text, while a lower value (e.g., 0.5) will generate more focused and conservative text. (Default: 0.9)
- **min_p**(float) 	Alternative to the top_p, and aims to ensure a balance of quality and variety. The parameter p represents the minimum probability for a token to be considered, relative to the probability of the most likely token. For example, with p=0.05 and the most likely token having a probability of 0.9, logits with a value less than 0.045 are filtered out. (Default: 0.0)

### TEMPLATE

`TEMPLATE` of the full prompt template to be passed into the model. It may include (optionally) a system message, a user's message and the response from the model. 
Note: syntax may be model specific. Template use GO [template_syntax](https://pkg.go.dev/text/template)
**Template variables**
- `{{ .System }}` The system message used to specify custom behavior.
- `{{ .Prompt }}` The user prompt message.
- `{{ .Response }}` The response from the model. When generating a response, text after this variable is omitted.

### SYSTEM
The `SYSTEM` instruction specifies the system message to be used in the template, if applicable.
```
SYSTEM """<system message>"""
```
### ADAPTER
The `ADAPTER` instruction is an optional instruction that specifies any LoRA adaptor that should apply to the base model. The value of this instruction should be an absolute path or a path relative to the Modelfile and the file must be in a GGML file format. The adapter should be tuned from the base model otherwise the behaviour is undefined.
```
ADAPTER ./ollama-lora.bin
```
### LICENSE
The `LICENSE` instruction allows you to specify the legal license under which the model used with this Modelfile is shared or distributed.
```
LICENSE """
<license text>
"""
```
### MESSAGE
The `MESSAGE` instruction allows you to specify a message history for the model to use when responding. Use multiple iterations of the MESSAGE command to build up a conversation which will guide the model to answer in a similar way.
```
MESSAGE <role> <message>
```
**Valid roles**
- **system** Alternate way of providing the SYSTEM message for the model.
- **user** An example message of what the user could have asked.
- **assistant** An example message of how the model should respond.

**Example conversation**
```
MESSAGE user Is Toronto in Canada?
MESSAGE assistant yes
MESSAGE user Is Sacramento in Canada?
MESSAGE assistant no
MESSAGE user Is Ontario in Canada?
MESSAGE assistant yes
```
### Notes
- the `Modelfile` is not case sensitive. In the examples, uppercase instructions are used to make it easier to distinguish it from arguments.
- Instructions can be in any order. In the examples, the `FROM` instruction is first to keep it easily readable.


---

For more informations about Modelfile visit [ollama-modelfile](https://github.com/ollama/ollama/blob/main/docs/modelfile.md)