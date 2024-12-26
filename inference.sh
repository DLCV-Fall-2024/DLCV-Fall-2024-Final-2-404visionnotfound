configs=(
    "sample/prompt0.yml"
    "sample/prompt1.yml"
    "sample/prompt2.yml"
    "sample/prompt3.yml"
)

for config in "${configs[@]}"; do
    echo "Inference $config"
    python3 sample.py --config_file $config
done
