import gradio as gr
import requests
import io
from PIL import Image, ImageEnhance

# Authorization
API_URL = "https://api-inference.huggingface.co/models/sd-community/sdxl-flash"
headers = {"Authorization": "Bearer hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response

def generate(prompt, brightness, contrast):
    response = query({
        "inputs": prompt,
    })

    if response.status_code == 200:
        try:
            image_bytes = response.content
            image = Image.open(io.BytesIO(image_bytes))

            enhancer = ImageEnhance.Brightness(image)
            image = enhancer.enhance(brightness)
            enhancer = ImageEnhance.Contrast(image)
            image = enhancer.enhance(contrast)
            return image
        except Exception as e:
            return f"Error processing image: {e}"
    elif response.status_code == 503:
        return "Model is currently loading. Please try again later."
    else:
        return f"Error: {response.status_code}, {response.text}"

iface = gr.Interface(fn=generate, inputs=["text", gr.Slider(0.5, 2.0, 1.0), gr.Slider(0.5, 2.0, 1.0)], outputs="image")
iface.launch(share=True)
