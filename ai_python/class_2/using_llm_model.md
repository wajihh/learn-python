To modify your code so that it calls an open-source language model instead of returning a mock response, you can use the `openai` package, which allows interaction with OpenAI's GPT models. Alternatively, if you prefer to use an entirely open-source model (like those available via Hugging Face), I'll also show you how to do that.

### Option 1: Using OpenAI's GPT Model (requires an API key)

1. **Install the OpenAI Python Client**:
   - Open the terminal in VS Code and install the `openai` package:
     ```bash
     pip install openai
     ```

2. **Update the `get_llm_response` Function**:
   - Replace the mock response with a call to OpenAI's GPT model.

   Here’s how you can modify your `helper_functions.py`:

   ```python
   import openai

   # Set up your OpenAI API key
   openai.api_key = "your-openai-api-key"

   def get_llm_response(input_text):
       response = openai.ChatCompletion.create(
           model="gpt-3.5-turbo",  # or "gpt-4" if you have access
           messages=[
               {"role": "system", "content": "You are a helpful assistant."},
               {"role": "user", "content": input_text},
           ]
       )
       return response['choices'][0]['message']['content']

   def print_llm_response(response):
       print(response)
   ```

   **Replace** `"your-openai-api-key"` with your actual OpenAI API key.

3. **Run Your Code**:
   - You can now use the `get_llm_response` function to interact with the GPT model.

   Example usage in `main.py`:
   ```python
   from helper_functions import print_llm_response, get_llm_response

   user_input = "What is AI?"
   response = get_llm_response(user_input)
   print_llm_response(response)
   ```

### Option 2: Using an Open-Source Model from Hugging Face (e.g., GPT-2)

1. **Install the Transformers and Torch Packages**:
   - Open the terminal and run:
     ```bash
     pip install transformers torch
     ```

2. **Update the `get_llm_response` Function**:
   - Modify the function to use a model from Hugging Face, like GPT-2.

   Here’s how you can do it:

   ```python
   from transformers import pipeline

   # Set up the model and tokenizer
   generator = pipeline("text-generation", model="gpt2")

   def get_llm_response(input_text):
       responses = generator(input_text, max_length=50, num_return_sequences=1)
       return responses[0]['generated_text']

   def print_llm_response(response):
       print(response)
   ```

3. **Run Your Code**:
   - This will now generate responses using GPT-2.

   Example usage in `main.py`:
   ```python
   from helper_functions import print_llm_response, get_llm_response

   user_input = "What is AI?"
   response = get_llm_response(user_input)
   print_llm_response(response)
   ```

### Notes:
- **API Costs**: If you use OpenAI’s GPT models, be mindful of API usage and costs.
- **Performance**: Open-source models like GPT-2 may not be as powerful as OpenAI's GPT-3.5/4, but they are free to use.

This should help you modify your code to interact with real language models. Let me know if you need further assistance!