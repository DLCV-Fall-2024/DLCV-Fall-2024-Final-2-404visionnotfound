from safetensors import safe_open

lora_weights_path = "/root/ziplora-pytorch/diffusers/examples/dreambooth/lora-trained-xl-autumn_rank_64/pytorch_lora_weights.safetensors"
with safe_open(lora_weights_path, framework="pt", device="cpu") as f:
    keys = f.keys()
    print(keys)
