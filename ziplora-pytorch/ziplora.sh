export MODEL_NAME="stabilityai/stable-diffusion-xl-base-1.0"

# for subject
export LORA_PATH="./pytorch_lora_weights_content_r64.safetensors"
export INSTANCE_DIR="./ziplora_dataset/content"
export PROMPT="a cat wearing wearable glasses"

# for style
export LORA_PATH2="./pytorch_lora_weights_style_r64.safetensors"
export INSTANCE_DIR2="./ziplora_dataset/style"
export PROMPT2="A photo of watercolour style"

# general
export OUTPUT_DIR="ziplora-sdxl-content-style-rank-64"
export VALID_PROMPT="a cat wearing wearable glasses in a watercolour style"


accelerate launch train_dreambooth_ziplora_sdxl.py \
  --pretrained_model_name_or_path=$MODEL_NAME  \
  --output_dir=$OUTPUT_DIR \
  --lora_name_or_path=$LORA_PATH \
  --instance_prompt="${PROMPT}" \
  --instance_data_dir=$INSTANCE_DIR \
  --lora_name_or_path_2=$LORA_PATH2 \
  --instance_prompt_2="${PROMPT2}" \
  --instance_data_dir_2=$INSTANCE_DIR2 \
  --resolution=512 \
  --train_batch_size=1 \
  --learning_rate=5e-5 \
  --similarity_lambda=0.01 \
  --lr_scheduler="constant" \
  --lr_warmup_steps=0 \
  --max_train_steps=100 \
  --validation_prompt="${VALID_PROMPT}" \
  --validation_epochs=20 \
  --seed="0" \
  --mixed_precision="bf16" \
  --report_to="wandb" \
  --gradient_checkpointing \
  --use_8bit_adam \
  --enable_xformers_memory_efficient_attention \