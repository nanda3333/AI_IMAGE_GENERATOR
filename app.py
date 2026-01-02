import os
import streamlit as st
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from PIL import Image
import io

# --------------------------------------------------
# Load environment variables
# --------------------------------------------------
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    st.error("HF_TOKEN not found. Please set it in your .env file.")
    st.stop()

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="AI Image Generator (SDXL)",
    page_icon="🎨",
    layout="centered"
)

# --------------------------------------------------
# Load Model Client (Cached)
# --------------------------------------------------
@st.cache_resource
def load_client():
    return InferenceClient(
        model="stabilityai/stable-diffusion-xl-base-1.0",
        token=HF_TOKEN
    )

client = load_client()

# --------------------------------------------------
# UI
# --------------------------------------------------
st.title("🎨 AI Image Generator")
st.markdown(
    "Generate high-quality images using **Stable Diffusion XL** "
    "via Hugging Face Inference API."
)

prompt = st.text_area(
    "Enter image prompt:",
    placeholder="Example: Professional product photo of wireless headphones",
    height=120
)

generate = st.button("Generate Image", type="primary", use_container_width=True)

if generate:
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating image... This may take 10–20 seconds."):
            try:
                image = client.text_to_image(prompt)

                # Convert to displayable format
                img_bytes = io.BytesIO()
                image.save(img_bytes, format="PNG")
                img_bytes.seek(0)

                st.subheader("Generated Image")
                st.image(img_bytes, use_container_width=True)

                st.download_button(
                    label="Download Image",
                    data=img_bytes,
                    file_name="generated_image.png",
                    mime="image/png"
                )

            except Exception as e:
                st.error(f"Image generation failed: {e}")

# --------------------------------------------------
# Footer
# --------------------------------------------------
with st.expander("ℹ️ Project Details"):
    st.write("Model: stabilityai/stable-diffusion-xl-base-1.0")
    st.write("Inference: Hugging Face Inference API")
    st.write("Execution: Local Streamlit Deployment")

