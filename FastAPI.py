from fastapi import FastAPI
from pydantic import BaseModel
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Initialize FastAPI app
app = FastAPI()
print(app)

# Load the model and tokenizer
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
print(model)
print(tokenizer)

# Define the input and output structure
class InputText(BaseModel):
    text: str

@app.post("/predict/")
def predict(input: InputText):
    inputs = tokenizer(input.text, return_tensors="pt")
    print(inputs)
    output = model.generate(inputs['input_ids'], max_length=100)
    print(output)
    result = tokenizer.decode(output[0], skip_special_tokens=True)
    print(result)
    return {"prediction": result}
