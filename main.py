from threading import Thread
from decibeli import dbs_script
from inregistrare_audio import audio_recording_script
from inregistrare_video import video_recording_script
from yt_random_video import youtube_video
from Merge_audio_video import Merge_audio_video
from internet_connection1 import check_internet


def main():
    youtube = Thread(target=youtube_video)
    video = Thread(target=video_recording_script)
    audio = Thread(target=audio_recording_script)
    decibels = Thread(target=dbs_script)
    FinalVid = Thread(target=Merge_audio_video)

    youtube.start()
    youtube.join()
    audio.start()
    video.start()
    video.join()
    audio.join()
    decibels.start()
    FinalVid.start()


main()
