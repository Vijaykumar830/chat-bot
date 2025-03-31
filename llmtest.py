import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the pre-trained model and tokenizer
model_name = "gpt2-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Generate text
prompt = "Write a Python program that takes an integer as input and prints 'Even' if the number is even, otherwise prints 'Odd'"
input_ids = tokenizer(prompt, return_tensors="pt").input_ids

# Generate attention mask (all tokens are attended to except padding)
attention_mask = torch.ones_like(input_ids)
attention_mask[:, tokenizer.pad_token_id] = 0

# Set pad token to EOS token for open-end generation
# This ensures proper termination of generation
pad_token_id = model.config.eos_token_id

# Generate poems
for _ in range(8):  # Generate 8 poems
  generated_text = model.generate(
      input_ids,
      max_length=100,
      num_beams=5,
      attention_mask=attention_mask,
      pad_token_id=pad_token_id
  )
  print(tokenizer.decode(generated_text[0], skip_special_tokens=True))