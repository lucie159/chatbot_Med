from models.init_model import model, tokenizer
import torch

def generate_response(user_input: str) -> str:
    prompt = f"### Question : {user_input.strip()}\n### Réponse :"
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=100)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded.split("### Réponse :")[-1].strip()