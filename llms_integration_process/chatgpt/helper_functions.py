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
