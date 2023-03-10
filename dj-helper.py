""" dj-helper.py

Downloads music from the internet for local use (e.g. for djing).

Prerequisites:
- youtube-dl
- ffmpeg

"""

import os
import sys
from termcolor import colored
import time

output_dir = '~/iCloud/Musik'

def download_audio(url: str):
    """Download audio from url.

    Args:
        url (str): URL to download from.

    """
    t_start = time.time()
    os.system(f"youtube-dl -o '{output_dir}/%(title)s.%(ext)s' -x --prefer-ffmpeg --audio-format mp3 {url}")
    t_end = time.time()
    print(colored(f"✓ ({(t_start-t_end):.1f} s)", "green"))


if __name__ == "__main__":
    while True:
        url = input("URL: ")
        if not url.startswith("https://www.youtube.com/watch?v="):
            print(colored("Invalid URL (does not start with 'https://www.youtube.com/watch?v=')", "red"))
            continue
        download_audio(url)