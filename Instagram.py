import subprocess
import re
import os
import uuid
import glob
import shutil

def ensure_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_shortcode_from_url(post_url):
    # Use regular expression to extract the shortcode
    match = re.search(r'/p/([^/]+)/|/reel/([^/]+)/', post_url)
    return match.group(1) or match.group(2) if match else ''

def download_instagram_post(post_url, destination_folder):
    try:
        shortcode = get_shortcode_from_url(post_url)

        # Run instaloader command with the specified arguments
        subprocess.run(["instaloader", "--", f"-{shortcode}"])

        # Get the list of downloaded files in the folder named after the shortcode
        downloaded_files_folder = glob.glob(f'-{shortcode}')
        if not downloaded_files_folder:
            print(f"No downloaded files found for {post_url}")
            return None

        downloaded_files = glob.glob(os.path.join(downloaded_files_folder[0], '*.mp4'))

        if downloaded_files:
            # Assuming there is only one file in the folder
            original_filename = downloaded_files[0]

            # Generate a new filename with UUID
            new_filename = f"vid_{uuid.uuid4().hex}.mp4"

            # Ensure the destination folder exists
            ensure_directory(destination_folder)

            # Move the file to the specified folder using shutil.move
            shutil.move(original_filename, os.path.join(destination_folder, new_filename))

            print(f"Downloaded {post_url} to {os.path.join(destination_folder, new_filename)}")
            return os.path.join(destination_folder, new_filename)
        else:
            print(f"No downloaded files found for {post_url}")
            return None
    except Exception as e:
        print(f"Failed to download Instagram post. Error: {str(e)}")
        return None
