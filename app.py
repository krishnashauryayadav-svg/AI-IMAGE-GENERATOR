import os
import requests
import io
from flask import Flask, render_template, request, send_file
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Model config
MODEL_ID = "RunDiffusion/Juggernaut-XL-v9"
HF_API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"
HF_TOKEN = os.getenv("HF_TOKEN") 

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_image():
    prompt = request.json.get("prompt", "")
    if not prompt: return "No Prompt", 400

    # Quality enhancer tags added
    enhanced_prompt = f"{prompt}, cyberrealistic, photorealistic, 8k, highly detailed"

    response = requests.post(HF_API_URL, headers=headers, json={"inputs": enhanced_prompt})
    if response.status_code == 200:
        return send_file(io.BytesIO(response.content), mimetype='image/png')
    return "Error", 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
