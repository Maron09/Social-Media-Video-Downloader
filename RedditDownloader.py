# RedditDownloader.py
from redvid import Downloader
import os
import glob
from urllib.parse import urlparse
import time
import shutil

def extract_username_from_url(url):
    parsed_url = urlparse(url)
    path_segments = parsed_url.path.split('/')
    username = path_segments[2] if len(path_segments) > 2 else None
    return username

def download_and_move(url, destination_folder):
    reddit = Downloader(max_q=True)
    reddit.url = url + ".json"  # Append .json to the URL
    reddit.download()

    downloaded_files = glob.glob('*.mp4')

    while not downloaded_files:
        time.sleep(1)
        downloaded_files = glob.glob('*.mp4')

    username = extract_username_from_url(reddit.url)

    if username and downloaded_files:
        original_filename = downloaded_files[0]
        new_filename = f"{username}.mp4"
        new_filepath = os.path.join(destination_folder, new_filename)

        # Move the file to the destination folder
        shutil.move(original_filename, new_filepath)

        return new_filepath
    else:
        return None

# Check if the destination folder exists, create it if not
if not os.path.exists('reddit_videos'):
    os.makedirs('reddit_videos')
