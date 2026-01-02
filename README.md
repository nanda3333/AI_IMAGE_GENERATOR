# AI_IMAGE_GENERATOR
This project is a Streamlit-based AI image generation application that allows users to generate high-quality images from text prompts using Stable Diffusion XL (SDXL) via the Hugging Face Inference API.

The application provides an intuitive web interface where users can enter a descriptive prompt, generate images in real time, preview the results, and download the generated images locally.

# 🚀 Key Features

Text-to-image generation using Stable Diffusion XL

Interactive Streamlit web interface

Secure authentication using Hugging Face access tokens

Cloud-based inference (no local GPU required)

Image preview and one-click download

Cached model client for improved performance

# 🧠 Model & Technology Stack

Model: Stability AI – Stable Diffusion XL (SDXL)

Inference: Hugging Face Inference API

Frontend & Backend: Streamlit

Language: Python

Environment Management: python-dotenv

Image Handling: Pillow (PIL)

# 🖥️ How It Works

The user enters a text prompt describing the desired image.

The application sends the prompt to the Hugging Face Inference API.

The SDXL model generates an image based on the prompt.

The generated image is displayed in the browser.

Users can download the image directly.

All inference is handled remotely, making the application lightweight and suitable for systems without GPUs.


# 🎯 Use Cases

AI-powered content creation

Rapid prototyping of visual ideas

Educational demonstrations of generative AI

Portfolio and academic projects

Prompt engineering experimentation

# ⚠️ Notes

This project uses cloud-based inference, so image generation time depends on network latency and API response time.

A valid Hugging Face token with inference access is required.

The .env file should not be committed to version control.

# 📌 Future Enhancements

Prompt history and image gallery

Negative prompt support

Image resolution and style selection

Seed control for reproducibility

Deployment to Hugging Face Spaces
