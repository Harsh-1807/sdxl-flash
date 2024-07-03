# SDXL-Flash: https://huggingface.co/sd-community/sdxl-flash

## Gradio Image Generation Interface

This repository provides a simple interface to generate images using the SDXL Flash model from the Hugging Face community, with options to adjust brightness and contrast.

## Setup Instructions

### Create a Virtual Environment for windows

```sh
python -m venv envname
.\envname\Scripts\activate

```
Install Required Packages
With the virtual environment activated, install the required packages using pip:

```sh
pip install requests gradio Pillow transformers huggingface_hub
python app.py
```
sh

The project runs on http://127.0.0.1:7860/. 


Example image::![Screenshot 2024-07-03 145955](https://github.com/Harsh-1807/sdxl-flash/assets/128303179/c4690527-153b-46be-9f16-3d4d0faf33c2)


