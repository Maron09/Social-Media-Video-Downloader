
![034699e0-8939-4c6a-bf4e-a5854a09181a](https://github.com/Maron09/Social-Media-Video-Downloader/assets/107930543/03b38bb9-a93d-42a4-b041-b9b346007414)


# Social Media Video Downloader

This Flask web application allows users to download videos from TikTok, Reddit, Instagram, and YouTube. Users can enter the URL of the video they wish to download, and the application will handle the download and provide a link to the saved video.

## Features

- **TikTok Video Download**: Download videos from TikTok and save them in a designated folder.
- **Reddit Video Download**: Download videos from Reddit and save them in a designated folder.
- **Instagram Media Download**: Download posts (videos and images) from Instagram and save them in a designated folder.
- **YouTube Video Download**: Download videos from YouTube and save them in a designated folder.

## Prerequisites

- Python 3.6 or higher
- Flask
- Video download libraries:
  - `TikTokDownloader`
  - `RedditDownloader`
  - `Instagram` (with necessary Instagram download functionality)
  - `YouTubeDownloader` (with necessary YouTube download functionality)

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/maron09/social-media-video-downloader.git
   cd social-media-video-downloader
   ```

2. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Set up folders:**

   Ensure the following folders exist in the root directory:
   - `reddit_videos`
   - `tiktok_videos`
   - `instagram_files`
   - `youtube_files`

   You can create them manually or through the command line:

   ```sh
   mkdir reddit_videos tiktok_videos instagram_files youtube_files
   ```

## Running the Application

To start the Flask application, run:

```sh
python app.py
```

This will start the server on `http://localhost:5000`.

## Usage

1. **Homepage**: Navigate to `http://localhost:5000/` to see the homepage.
2. **Download Page**: Select the platform (TikTok, Reddit, Instagram, or YouTube) from the navigation menu.
3. **Enter URL**: On the selected platform's page, enter the video URL and click the download button.
4. **Download Link**: If the download is successful, a link to the downloaded video will be provided.

## Folder Structure

- **app.py**: The main Flask application file.
- **templates/**: Contains HTML templates for the homepage and other pages.
  - **homepage.html**: The main homepage template.
  - **TikTok/tiktok_page.html**: Template for the TikTok download page.
  - **Reddit/reddit_page.html**: Template for the Reddit download page.
  - **Instagram/instagram_page.html**: Template for the Instagram download page.
  - **Youtube/youtube_page.html**: Template for the YouTube download page.
  - **download.html**: Template for displaying the download link.
- **reddit_videos/**: Folder where Reddit videos are saved.
- **tiktok_videos/**: Folder where TikTok videos are saved.
- **instagram_files/**: Folder where Instagram media files are saved.
- **youtube_files/**: Folder where YouTube videos are saved.

## Error Handling

If the video URL is invalid or if the download fails, an error message will be displayed on the homepage.

## Logging

Errors during the download process are logged for troubleshooting. Check the Flask application logs for more details if something goes wrong.


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any features or bug fixes.

## Contact

For any questions or support, please open an issue in the repository or contact the project maintainer.


- **Email**: chimarokeonyebi@gmail.com

---

This README provides an overview of the project, setup instructions, and usage details to help you get started with the social media video downloader web application.
