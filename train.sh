#!/bin/bash

configs=(
    "train_data_file/cat2.yml"
    "train_data_file/dog.yml"
    "train_data_file/dog6.yml"
    "train_data_file/flower_1.yml"
    "train_data_file/pet_cat1.yml"
    "train_data_file/vase.yml"
    "train_data_file/watercolor.yml"
    "train_data_file/wearable_glasses.yml"
)

for config in "${configs[@]}"; do
    echo "Training $config"
    python train_edlora.py -opt "$config"
done
