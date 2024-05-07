import os
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from datetime import datetime
from urllib.parse import urlparse
import shutil  # Import shutil for file operations

def ensure_downloads_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def extract_username_from_link(link):
    # Extract username from TikTok video link
    username = link.split('@')[1].split('/')[0]
    return username

def download_recent_video(link, server_dir):
    # Extract username from TikTok video link
    username = extract_username_from_link(link)

    ensure_downloads_directory("downloads")  # Ensure the "downloads" directory exists

    cookies = {
        '_ga': 'GA1.2.1922949325.1677776852',
        '_gid': 'GA1.2.2014378703.1677776852',
        '__gads': 'ID=f4cda8988d895a57-223f30f029dc0031:T=1677776853:RT=1677776853:S=ALNI_MZ3tLPUJ7FgeEyfTkZOclsQkY8QWQ',
        '__gpi': 'UID=00000be052f713af:T=1677776853:RT=1677776853:S=ALNI_MbvRQYg4RcYOg5bgCMetpAbh-8N7g',
        '_gat_UA-3524196-6': '1',
    }

    headers = {
        'authority': 'ssstik.io',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'hx-current-url': 'https://ssstik.io/en',
        'hx-request': 'true',
        'hx-target': 'target',
        'hx-trigger': '_gcaptcha_pt',
        'origin': 'https://ssstik.io',
        'referer': 'https://ssstik.io/en',
        'sec-ch-ua': '"Not A(Brand";v="24", "Chromium";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    params = {
        'url': 'dl',
    }

    data = {
        'id': link,
        'locale': 'en',
        'tt': 'MlNhdDQ1',
    }
    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
    downloadSoup = bs(response.text, 'html.parser')
    download_link = downloadSoup.find('a')

    if download_link is not None:
        downloadURL = download_link.get('href')
        filename = f"{username}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
        filepath = os.path.join("downloads", filename)

        mp4_file = urlopen(downloadURL)
        with open(filepath, "wb") as f:
            while True:
                data = mp4_file.read(4096)
                if data:
                    f.write(data)
                else:
                    break

        print(f"Downloaded {link} to {filepath}")
        return link, username, filepath
    else:
        print(f"Failed to retrieve download link for {link}")
        return None

def download_and_move_vid(url, server_dir):
    # Download the video and move it to the server directory
    result = download_recent_video(url, server_dir)
    if result:
        _, _, filepath = result
        destination = os.path.join(server_dir, os.path.basename(filepath))
        shutil.move(filepath, destination)
        print(f"Moved {filepath} to {destination}")
        return destination
    else:
        return None
