## :book: Object Dependency-Aware 3D Scene Graph Prediction for Point Cloud based onMultimodal Feature Learning
<image src="demo.png" width="100%">

# Introduction
This is a release of the code of our paper **_Object Dependency-Aware 3D Scene Graph Prediction for Point Cloud based on Multimodal Feature Learning_**.

Authors:
Shibin Li*, 
Shengnan Ke, 
Jun Gong, 
Shengjun Tang, 
Lingxiang Liu, 
Jiangjun Luo, 
Ruisheng Wang, 
Bing WANG

[[code]](https://github.com/Lsb0113/ODA3SG)

# Dependencies
```bash
conda create -n vlsat python=3.8
conda activate ODA3SG
pip install -r requirement.txt
pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113
pip install torch-scatter -f https://pytorch-geometric.com/whl/torch-1.12.1+cu113.html
pip install torch-sparse -f https://pytorch-geometric.com/whl/torch-1.12.1+cu113.html
pip install torch-spline-conv -f https://pytorch-geometric.com/whl/torch-1.12.1+cu113.html
pip install torch-geometric
pip install git+https://github.com/openai/CLIP.git
```

# Prepare the data
A. Download 3Rscan and 3DSSG-Sub Annotation, you can follow [3DSSG](https://github.com/ShunChengWu/3DSSG#preparation). Alternatively, you can download the dataset as follows:
```bash
# download dataset to the target folder
python dl_data.py
# unzip dataset
python unzip.py
```
B. Generate 2D Multi View Image
```bash
# you should motify the path in pointcloud2image.py into your own path
python data/pointcloud2image.py
```

C. You should arrange the file location like this
```
data
  3DSSG_subset
    relations.txt
    classes.txt
    
  3RScan
    0a4b8ef6-a83a-21f2-8672-dce34dd0d7ca
      multi_view
      labels.instances.align.annotated.v2.ply
    ...  
      
```

D. Train your own clip adapter 

``` python clip_adapter/main.py ```

or just use the checkpoint 

``` clip_adapter/checkpoint/origin_mean.pth ```

# Run Code
```bash
python main.py
```
In this repo, we have provided a default [config](https://github.com/Lsb0113/ViT3SG/blob/main/config/mmgnet.json)

# Acknowledgement
This repository is partly based on [VL-SAT](https://github.com/wz7in/CVPR2023-VLSAT) and [CLIP](https://github.com/openai/CLIP) repositories.
