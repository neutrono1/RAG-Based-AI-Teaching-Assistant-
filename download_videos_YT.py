import yt_dlp
import os

def download_playlist_videos():
    playlist_url = "https://www.youtube.com/playlist?list=PLBlnK6fEyqRhG6s3jYIU48CqsT5cyiDTO"
    download_folder = "VIDEOS"

    os.makedirs(download_folder, exist_ok=True)

    ydl_opts = {
        # File naming
        "outtmpl": f"{download_folder}/%(playlist_index)s - %(title)s.%(ext)s",
                    # .ext means the file extension 
        # Reliable format selection
        "format": "bv*+ba/b",

        # Download range
        "playlist_items": "1-15",

        # Merge
        "merge_output_format": "mp4",

        #  JS runtime (correct format)
        "js_runtimes": {
            "node": {}
        },

        # Stability options
        "retries": 10,
        "fragment_retries": 10,
        "sleep_interval": 1,
        "max_sleep_interval": 3,

        # Less noise, still informative
        "quiet": False,
        "no_warnings": False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

    print(" Downloaded first 15 videos successfully")

download_playlist_videos()
