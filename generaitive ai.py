from transformers import pipeline

prompt = input("enter prompt:")
Generator = pipeline('text-generation',model='gpt2')
result = Generator(prompt, max_length=100, num_return_sequences=1)
print(result[0]['generated_text'])