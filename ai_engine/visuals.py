from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

def create_frame(text, output_path):
    img = Image.new("RGB", (1280, 720), color=(20, 20, 20))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 48)
    except:
        font = ImageFont.load_default()

    wrapped_text = textwrap.fill(text, width=40)

    bbox = draw.multiline_textbbox((0, 0), wrapped_text, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]

    x = (1280 - w) // 2
    y = (720 - h) // 2

    draw.multiline_text(
        (x, y),
        wrapped_text,
        fill="white",
        font=font,
        align="center"
    )

    img.save(output_path)


def generate_images(sentences, output_dir="output/images"):
    os.makedirs(output_dir, exist_ok=True)

    image_paths = []
    for i, sentence in enumerate(sentences):
        path = f"{output_dir}/frame_{i}.png"
        create_frame(sentence, path)
        image_paths.append(path)

    return image_paths
