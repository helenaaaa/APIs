from fastapi import FastAPI
from pydantic import BaseModel
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Initialize FastAPI app
app = FastAPI()

# Load the model and tokenizer
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Define the input and output structure
class InputText(BaseModel):
    text: str

@app.post("/predict/")
def predict(input: InputText):
    inputs = tokenizer(input.text, return_tensors="pt")
    output = model.generate(inputs['input_ids'], max_length=100)
    result = tokenizer.decode(output[0], skip_special_tokens=True)
    return {"prediction": result}
