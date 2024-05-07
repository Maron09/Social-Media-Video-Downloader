from pytube import YouTube
import uuid
import os



def download_youtube_video(video_link, destination_folder):
    try:
        yt = YouTube(video_link)
        video = yt.streams.get_highest_resolution()
        video.download(output_path=destination_folder)
        destination = os.path.join(destination_folder)
        return destination
    except Exception as e:
        print(f"Failed to download YouTube video. Error: {str(e)}")
        return None