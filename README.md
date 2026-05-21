# 🎨 CyberRealistic AI Image Generator

A lightweight, powerful, and **100% free** AI Image Generator web application. This project uses a **Python Flask** backend to integrate Hugging Face's high-quality open-source models, paired with a modern, responsive **Tailwind CSS** frontend.

---

## ⚠️ CRITICAL SETUP NOTE (⚠️ ज़रूरी सूचना)
Before running or deploying this project, you **MUST** create a local environment file to store your Hugging Face API token securely. Do not upload your token directly to GitHub!

1. Create a file named `.env` in the root directory.
2. Generate a free **Read Access Token** from your [Hugging Face Settings](https://huggingface.co).
3. Paste it inside the `.env` file exactly like this:
   ```env
   HF_TOKEN=your_actual_huggingface_token_here
   ```

---

## ✨ Features
* **Hyper-Realistic Output:** Pre-configured with the premium `SG161222/RealVisXL_V4.0` model for photorealistic images.
* **100% Free & Unlimited:** No paid OpenAI subscription needed. Completely open-source API handling.
* **Modern UI:** Built using a sleek dark-themed layout with pure HTML, Tailwind CSS, and asynchronous JavaScript.
* **Production Ready:** Pre-configured for instant deployment on platforms like Render.

## 🛠️ Tech Stack
- **Backend:** Python, Flask
- **AI Engine:** Hugging Face Inference API (`RealVisXL_V4.0`)
- **Frontend:** HTML5, JavaScript (Fetch API), Tailwind CSS

## 📦 Local Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com
   cd ai-image-generator
   ```

2. **Create and Activate Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup Environment Variables:**
   * Create the `.env` file as shown in the **Critical Setup Note** section above.

5. **Run the Application:**
   ```bash
   python app.py
   ```
   * Open your browser and navigate to `http://127.0.0.1:5000`

---

## 🚀 How to Deploy on Render

Since this app uses Python for both backend logic and serving frontend files, deployment takes less than 2 minutes:

1. Push your updated code to your GitHub repository (ensure `.env` is ignored via `.gitignore`).
2. Go to [Render Dashboard](https://render.com) and click **New +** -> **Web Service**.
3. Connect your GitHub repository.
4. Configure the service settings:
   * **Runtime:** `Python`
   * **Build Command:** `pip install -r requirements.txt`
   * **Start Command:** `gunicorn app:app`
5. Click on the **Environment Variables** tab and add:
   * **Key:** `HF_TOKEN`
   * **Value:** *[Your Hugging Face Access Token]*
6. Click **Deploy Web Service**. Done! 🎉
