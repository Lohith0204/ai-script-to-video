from moviepy import ImageClip, AudioFileClip, concatenate_videoclips

def create_video(image_paths, audio_path, output_path, fps=24):
    audio = AudioFileClip(audio_path)

    image_duration = audio.duration / len(image_paths)

    clips = []
    for img in image_paths:
        clip = ImageClip(img).with_duration(image_duration)
        clips.append(clip)

    video = concatenate_videoclips(clips, method="compose")
    video = video.with_audio(audio)

    video.write_videofile(
        output_path,
        fps=fps,
        codec="libx264",
        audio_codec="aac"
    )
