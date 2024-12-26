# DLCV Final Project ( Multiple Concept Personalization )

# Usage
To start working on this final project, you should clone this repository into your local machine by the following command:

    git clone https://github.com/DLCV-Fall-2024/DLCV-Fall-2024-Final-2-<team name>.git
  
Note that you should replace `<team_name>` with your own team name.

For more details, please click [this link](https://docs.google.com/presentation/d/1eeXx_dL0OgkDn9_lhXnimTHrE6OYvAiiVOBwo2CTVOQ/edit?usp=sharing) to view the slides of Final Project - Multiple Concept Personalization. **The introduction video for final project can be accessed in the slides.**


# How to run your code?
* Please create the environment and download the training pretrain model and inference checkpoint
```bash
pip install -r requirements.txt
bash download_data.sh
cd experiments/pretrained_models
git-lfs clone https://huggingface.co/windwhinny/chilloutmix.git
```
* Training output will be saved in experiments folder with name "8EDLORA_<TOKEN_NAME>"
* Inference output will be saved in outputs folder
* If you want to inference your training ckpt please replace the ckpt in inf folder with your own
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
