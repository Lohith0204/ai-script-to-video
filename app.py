import streamlit as st
from ai_engine.script_processor import split_script
from ai_engine.audio import generate_audio
from ai_engine.visuals import create_frame
from ai_engine.video import create_video
import os

st.title("Script to Video Generator")

script = st.text_area("Enter your script")

if st.button("Generate Video"):

    if not script.strip():
        st.warning("Please enter a script")
        st.stop()

    sentences = split_script(script)

    os.makedirs("assets/images", exist_ok=True)
    os.makedirs("assets/audio", exist_ok=True)
    os.makedirs("output", exist_ok=True)

    audio_path = "assets/audio/narration.mp3"
    generate_audio(script, audio_path)

    image_paths = []
    for i, sentence in enumerate(sentences):
        img_path = f"assets/images/frame_{i}.png"
        create_frame(sentence, img_path)
        image_paths.append(img_path)

    output_path = "output/final_video.mp4"
    create_video(image_paths, audio_path, output_path)

    st.success("Video generated successfully!")
    st.video(output_path)
