import streamlit as st
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

st.set_page_config(
    page_title="AI Image Generator",
    page_icon="🎨"
)

st.title("🎨 AI Image Generator")
st.write("Generate images using AI from a text prompt.")

token = os.getenv("HF_TOKEN")

if not token:
    st.error("Hugging Face token not found. Check your .env file.")
    st.stop()

client = InferenceClient(
    provider="auto",
    api_key=token
)

prompt = st.text_input(
    "Enter your prompt:",
    "A cute cat sitting in a beautiful garden"
)

if st.button("🎨 Generate Image"):

    if prompt.strip():

        with st.spinner("Generating image..."):
            image = client.text_to_image(
                prompt,
                model="black-forest-labs/FLUX.1-schnell"
            )

        st.success("Image generated successfully! 🎉")
        st.image(image, caption=prompt, use_container_width=True)

    else:
        st.warning("Please enter a prompt.")