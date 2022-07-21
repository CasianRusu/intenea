from moviepy.editor import *


def Merge_audio_video():
    clip = VideoFileClip("output.mp4")
    clip = clip.subclip(0, 25)
    audio = AudioFileClip("recorded.wav").subclip(1, 25)
    videoclip = clip.set_audio(audio)
    videoclip.ipython_display()
