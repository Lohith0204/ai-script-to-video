# AI Script to Video Generator (v1.0)

## Overview
AI Script2Video is a Python-based application that converts a text script into a video by generating audio narration and corresponding visual frames, then combining them into a final video output.
The project focuses on building a simple, modular, and extensible pipeline for script-based video generation without training custom AI models.

This version (v1.0) emphasizes clarity, modularity, and correctness, making it easy to enhance in future versions.

## Features
- Convert text scripts into structured sentences
- Generate narration audio from text
- Create visual frames based on script content
- Combine audio and visuals into a final video
- Modular design for easy upgrades
- Simple and beginner-friendly pipeline

## Tech Stack
- Python
- Streamlit
- gTTS (Google Text-to-Speech)
- OpenCV
- MoviePy
- NumPy

## Project Structure
AI SCRIPT2VIDEO/
│
├── app.py                   # Streamlit application entry point
├── requirements.txt         # Project dependencies
├── README.md                # Project documentation
│
├── ai_engine/
│   ├── audio.py             # Text-to-speech audio generation
│   ├── script_processor.py  # Script cleaning and sentence processing
│   ├── visuals.py           # Visual frame generation logic
│   ├── video.py             # Video creation from frames and audio
│   └── __pycache__/
│
├── assets/
│   ├── audio/
│   │   └── narration.mp3    # Generated narration audio
│   │
│   └── images/
│       ├── frame_0.png      # Generated visual frame
│       └── frame_1.png
│
├── output/
│   └── final_video.mp4      # Generated output video
│
├── screenshots/             # Application screenshots
└── venv/                    # Virtual environment (ignored in Git)


## Screenshots

### Application Interface
![Application Interface](<screenshots/Screenshot 2025-12-26 103311.png>)

### Script Input
![Script Input](<screenshots/Screenshot 2025-12-26 103551.png>)

### Video Output
![Video Output](<screenshots/Screenshot 2025-12-26 103644.png>)


## How It Works
1. The user provides a text script through the application interface.
2. The script is cleaned and split into meaningful sentences.
3. Each sentence is converted into audio narration.
4. Corresponding visual frames are generated for the script.
5. Frames and narration audio are merged to produce a final video.

## Installation & Setup
1. Open your IDE (VS Code is recommended).
2. Clone or download the project files to your local system.
3. Create a virtual environment to avoid dependency conflicts:
   ```bash
   python -m venv venv
   venv\Scripts\activate
4. Install the required dependencies:
    pip install -r requirements.txt
5. Run the application:
    streamlit run app.py

## Usage
This application can be used to convert a written script into a complete video. Users simply provide a text script through the application interface. The system processes the script, generates narration audio, creates corresponding visual frames, and combines them into a final video. The generated video is then saved and displayed, allowing users to quickly transform text content into an engaging visual format.

## Future Improvements
AI-based image generation for visuals
Better synchronization between audio and frames
Support for longer scripts
Scene-level video generation
Enhanced UI and customization options

## Learning Outcomes
This project helped me understand how script-based video generation pipelines work in real-world applications.
I learned how to process text, generate audio, create visual assets, and merge multiple components into a single video output.The project strengthened my skills in Python modular design, media processing, and AI tool integration.