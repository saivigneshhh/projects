# Install required libraries
!pip install gradio requests pillow

import requests
import gradio as gr
import base64
import io
from PIL import Image

# Hugging Face API Configuration
API_URL = "https://api-inference.huggingface.co/models/black-forestlabs/FLUX.1-schnell"
API_KEY = #api key goes here
# Restricted Words List
RESTRICTED_WORDS = [
    "18+", "adult", "explicit", "nsfw", "inappropriate", "porn", "sex", "nude", "naked",
    "erotic", "fetish", "hardcore", "provocative", "xxx", "violent", "gore", "gruesome",
    "torture", "disturbing", "abuse", "racist", "hateful", "offensive", "vulgar", "obscene",
    "lewd", "suggestive", "graphic", "intimate", "sensitive", "taboo", "incest", "rape",
    "molestation", "bestiality", "pedophilia", "drug", "weapon", "assault", "murder",
    "suicide", "self-harm", "abduction", "trafficking"
]

# API Headers
headers = {"Authorization": f"Bearer {API_KEY}"}

# Query Hugging Face API
def query_huggingface_api(prompt):
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)
    try:
        print("Response status code:", response.status_code)
        response_json = response.json()
        print("API response content:", response_json)  # Debugging the API response

        if 'image' in response_json:
            print("Image key found in response")
            image_data = base64.b64decode(response_json['image'])
            return Image.open(io.BytesIO(image_data))
        elif 'url' in response_json:
            print("URL key found in response")
            image_url = response_json['url']
            image_response = requests.get(image_url)
            return Image.open(io.BytesIO(image_response.content))
        else:
            print("Unexpected response format:", response_json)
            return None
    except Exception as e:
        print(f"Error during API call: {e}")
        return None

# Check for Inappropriate Content
def check_for_inappropriate_content(prompt):
    return not any(word in prompt.lower() for word in RESTRICTED_WORDS)

# Generate Image Function
def generate_image(prompt):
    if not check_for_inappropriate_content(prompt):
        return "The prompt contains inappropriate content. Please enter a valid prompt."

    print("Generating image for prompt:", prompt)
    result = query_huggingface_api(prompt)
    if isinstance(result, Image.Image):  # Check if a valid image was returned
        result.save("output_image.png")  # Save image locally for debugging
        print("Image saved as output_image.png")
        return result
    return "Failed to generate image. Check logs for details."

# Gradio Interface
interface = gr.Interface(
    fn=generate_image,
    inputs="text",
    outputs="image",
    title="Text to Image Generator",
    description="Enter a prompt to generate an image using the FLUX model via Hugging Face API."
)

# Launch the Interface
interface.launch()