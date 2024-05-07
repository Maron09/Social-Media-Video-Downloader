# app.py
from flask import Flask, render_template, request, redirect, url_for
from TikTokDownloader import download_and_move_vid
from RedditDownloader import download_and_move
from Instagram import *
from YouTubeDownloader import *

app = Flask(__name__)

# Set the destination folder for hosting Reddit videos
REDDIT_VIDEO_FOLDER = 'reddit_videos'
TIKTOK_VIDEO_FOLDER = 'tiktok_videos'
INSTAGRAM_FOLDER = 'instagram_files'
YOUTUBE_FOLDER = 'youtube_files'

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/tiktok')
def tiktok_page():
    return render_template('TikTok/tiktok_page.html')

@app.route('/reddit_page')
def reddit_page():
    return render_template('Reddit/reddit_page.html')

@app.route('/instagram')
def instagram_page():
    return render_template('Instagram/instagram_page.html')

@app.route('/youtube')
def youtube_page():
    return render_template('Youtube/youtube_page.html')

@app.route('/download', methods=['POST'])
def download():
    try:
        video_link = request.form.get('video_link')

        if video_link:
            # Check if the link is from TikTok or Reddit
            if 'tiktok.com' in video_link:
                download_url = f'http://localhost:8080/{download_and_move_vid(video_link, TIKTOK_VIDEO_FOLDER)}'
                back_url = url_for('tiktok_page')
            elif 'reddit.com' in video_link:
                download_url = f'http://localhost:8080/{download_and_move(video_link, REDDIT_VIDEO_FOLDER)}'
                back_url = url_for('reddit_page')
            elif 'instagram.com' in video_link:
                download_url = f'http://localhost:8080/{download_instagram_post(video_link, INSTAGRAM_FOLDER)}'
                back_url = url_for('instagram_page')
            elif 'youtube.com' in video_link:
                download_url = f'http://localhost:8080/{download_youtube_video(video_link, YOUTUBE_FOLDER)}'
                back_url = url_for('youtube_page')
            else:
                return render_template('homepage.html', message="Invalid video link")

            if download_url:
                return render_template('download.html', download_url=download_url, back_url=back_url)
            else:
                return render_template('homepage.html', message=f"Video {video_link} already downloaded.")
        else:
            return render_template('homepage.html', message="Invalid video link")

    except Exception as e:
        app.logger.error(f"Failed to download video. Error: {str(e)}")
        return render_template('homepage.html', message="Failed to download video. Please try again later.")

if __name__ == '__main__':
    app.run(debug=True)


