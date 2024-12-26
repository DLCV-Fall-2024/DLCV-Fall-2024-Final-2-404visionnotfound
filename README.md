# DLCV Final Project ( Multiple Concept Personalization )

# Usage
To start working on this final project, you should clone this repository into your local machine by the following command:

    git clone https://github.com/DLCV-Fall-2024/DLCV-Fall-2024-Final-2-404visionnotfound.git



For more details, please click [this link](https://docs.google.com/presentation/d/1eeXx_dL0OgkDn9_lhXnimTHrE6OYvAiiVOBwo2CTVOQ/edit?usp=sharing) to view the slides of Final Project - Multiple Concept Personalization. **The introduction video for final project can be accessed in the slides.**


# How to prepare your training and inference?
* Please create the environment and download the training pretrain model and inference checkpoint

## Execute
### Create conda environment
```shell
conda create -n ConceptConductor python=3.10 -y
conda activate ConceptConductor
```
### Install dependencies and download dataset and checkpoints (At root directory)
```shell
pip install torch==2.5.0 torchvision==0.20.0 torchaudio==2.5.0 --index-url https://download.pytorch.org/whl/cu121
python -m pip install -r requirements.txt
bash download_data.sh
```
### Download pretrained models
```bash
conda install -c conda-forge git-lfs -y
git lfs install

mkdir -p experiments/pretrained_models # -p make parent dir if needed
cd experiments/pretrained_models
git-lfs clone https://huggingface.co/windwhinny/chilloutmix.git
apt-get update
apt-get install -y libgl1-mesa-glx
# back to root directory
cd ..
cd ..
```

# How to train and inference?
* Training output will be saved in "./experiments/8EDLORA_<TOKEN_NAME>"
* Inference output will be saved in "./outputs/prompt<PROMPT_INDEX>/inference_results/samples"
* If you want to inference your training ckpt please replace the ckpt in inf folder with your own ckpt in experiments folder
## Execute training and inference (At root directory)
```shell script=
bash train.sh
bash inference.sh
```

# Submission Rules
### Deadline
113/12/26 (Thur.) 23:59 (GMT+8)

# Q&A
If you have any problems related to Final Project, you may
- Use TA hours
- Contact TAs by e-mail ([ntudlcv@gmail.com](mailto:ntudlcv@gmail.com))
- Post your question under `[Final challenge 2] Discussion` section in NTU Cool Discussion
