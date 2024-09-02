
from transformers import pipeline

# Set up the model and tokenizer with specific parameters to avoid warnings
generator = pipeline(
    "text-generation",
    model="Meta-Llama-3.1-70B-Instruct",
    clean_up_tokenization_spaces=True,  # Explicitly set to avoid future warning
    pad_token_id=50256  # Explicitly set pad_token_id to eos_token_id
)

def get_llm_response(input_text):
    # Specify truncation to avoid truncation warning
    responses = generator(
        input_text,
        max_length=50,
        num_return_sequences=1,
        truncation=True  # Explicitly set truncation
    )
    return responses[0]['generated_text']

def print_llm_response(response):
    print(response)
