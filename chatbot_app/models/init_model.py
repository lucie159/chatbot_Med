import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

model_path = "falcon-lora-finetuned"
tokenizer = AutoTokenizer.from_pretrained(model_path)
base_model = AutoModelForCausalLM.from_pretrained(model_path, device_map={"": torch.cuda.current_device()})
model = PeftModel.from_pretrained(base_model, model_path)
model.eval()