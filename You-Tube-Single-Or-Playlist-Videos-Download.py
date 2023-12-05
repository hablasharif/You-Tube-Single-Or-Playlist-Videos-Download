#############################################################

from pytube import YouTube
# from tqdm import tqdm
# import re
# import requests

# # List of YouTube URLs
# urls = [
# "https://www.youtube.com/watch?v=rsIInabhd2E&list=PLNMnAEqLBwmodUM0HlExxtYERNS2YARhW&index=32&pp=iAQB","https://www.youtube.com/watch?v=8llCBZ3ymwg&list=PLNMnAEqLBwmodUM0HlExxtYERNS2YARhW&index=33&pp=iAQB","https://www.youtube.com/watch?v=GvX7hhyLhvo&list=PLNMnAEqLBwmodUM0HlExxtYERNS2YARhW&index=34&pp=iAQB","https://www.youtube.com/watch?v=HyODBevBzRs&list=PLNMnAEqLBwmodUM0HlExxtYERNS2YARhW&index=35&pp=iAQB","https://www.youtube.com/watch?v=xTDCThaWqX0&list=PLNMnAEqLBwmodUM0HlExxtYERNS2YARhW&index=36&pp=iAQB","https://www.youtube.com/watch?v=znY_TZXqmCo&list=PLNMnAEqLBwmodUM0HlExxtYERNS2YARhW&index=37&pp=iAQB","https://www.youtube.com/watch?v=y-AZQhvA5Wk&list=PLNMnAEqLBwmodUM0HlExxtYERNS2YARhW&index=38&pp=iAQB","https://www.youtube.com/watch?v=LlTUJpBvzLM&list=PLNMnAEqLBwmodUM0HlExxtYERNS2YARhW&index=39&pp=iAQB","https://www.youtube.com/watch?v=2H_3-lxP7-s&list=PLNMnAEqLBwmodUM0HlExxtYERNS2YARhW&index=40&pp=iAQB","https://www.youtube.com/watch?v=R8CB2XFB0mA&list=PLNMnAEqLBwmodUM0HlExxtYERNS2YARhW&index=41&pp=iAQB","https://www.youtube.com/watch?v=8ZTq78ggLZk&list=PLNMnAEqLBwmodUM0HlExxtYERNS2YARhW&index=42&pp=iAQB","https://www.youtube.com/watch?v=gnIaxr_Dixk&list=PLNMnAEqLBwmodUM0HlExxtYERNS2YARhW&index=43&pp=iAQB","https://www.youtube.com/watch?v=ep3IrPvtYes&list=PLNMnAEqLBwmodUM0HlExxtYERNS2YARhW&index=44&pp=iAQB","https://www.youtube.com/watch?v=eKezCc5lczg&list=PLNMnAEqLBwmodUM0HlExxtYERNS2YARhW&index=45&pp=iAQB","https://www.youtube.com/watch?v=n_YPb0f7yF0&list=PLNMnAEqLBwmodUM0HlExxtYERNS2YARhW&index=46&pp=iAQB","https://www.youtube.com/watch?v=VECvy45rW3Y&list=PLNMnAEqLBwmodUM0HlExxtYERNS2YARhW&index=47&pp=iAQB","https://www.youtube.com/watch?v=VpyNZFn644k&list=PLNMnAEqLBwmodUM0HlExxtYERNS2YARhW&index=48&pp=iAQB","https://www.youtube.com/watch?v=K34J8KMRLUY&list=PLNMnAEqLBwmodUM0HlExxtYERNS2YARhW&index=49&pp=iAQB","https://www.youtube.com/watch?v=pYtLFLdC-C8&list=PLNMnAEqLBwmodUM0HlExxtYERNS2YARhW&index=50&pp=iAQB"
# ]

# # Output folder
# output_folder = 'downloaded_videos'

# # Create the output folder if it doesn't exist
# import os
# os.makedirs(output_folder, exist_ok=True)

# def download_highest_resolution_video(url):
#     try:
#         yt = YouTube(url)
#         streams = yt.streams.filter(progressive=True, file_extension='mp4')
        
#         # Sort streams by resolution in descending order to get the highest resolution
#         streams = sorted(streams, key=lambda x: int(x.resolution[:-1]), reverse=True)
        
#         if not streams:
#             raise Exception(f"No suitable stream found for {yt.title}")
        
#         stream = streams[0]  # Get the first (highest resolution) stream
#         video_title = re.sub(r'[\/:*?"<>|]', '', yt.title)  # Remove invalid characters
#         print(f"Downloading: {video_title} ({stream.resolution})")

#         file_path = os.path.join(output_folder, f"{video_title}.mp4")
#         response = requests.get(stream.url, stream=True)

#         total_size = int(response.headers.get('content-length', 0))
#         block_size = 1024
#         progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024, dynamic_ncols=True)
        
#         with open(file_path, 'wb') as file:
#             for data in response.iter_content(block_size):
#                 file.write(data)
#                 progress_bar.update(len(data))
        
#         progress_bar.close()
#         print(f"Downloaded: {video_title}")
#     except Exception as e:
#         print(f"Error downloading {url}: {e}")

# # Download videos with the highest available resolution for each URL
# for url in urls:
#     download_highest_resolution_video(url)
#################################################
# import pytube
# import tqdm
# import os  # Import the 'os' module for file and directory operations

# def download_youtube_video(video_url):
#     """Downloads a single YouTube video to the 'Hablu Progmmer javascript videos' folder.

#     Args:
#         video_url: The URL of the YouTube video to download.
#     """
#     # Create the 'Hablu Progmmer javascript videos' folder if it doesn't exist
#     if not os.path.exists('Hablu Progmmer javascript videos'):
#         os.makedirs('Hablu Progmmer javascript videos')
    
#     # Change the working directory to the 'Ani2sul Islam' folder
#     os.chdir('Hablu Progmmer javascript videos')
    
#     video = pytube.YouTube(video_url)
#     video.streams.get_highest_resolution().download()

# def download_youtube_playlist(playlist_url):
#     """Downloads a YouTube playlist to the 'Hablu Progmmer javascript videos' folder.

#     Args:
#         playlist_url: The URL of the YouTube playlist to download.
#     """
#     # Create the 'Hablu Progmmer javascript videos' folder if it doesn't exist
#     if not os.path.exists('Hablu Progmmer javascript videos'):
#         os.makedirs('Hablu Progmmer javascript videos')
    
#     # Change the working directory to the 'Hablu Progmmer javascript videos' folder
#     os.chdir('Hablu Progmmer javascript videos')
    
#     playlist = pytube.Playlist(playlist_url)
#     for video in tqdm.tqdm(playlist.videos):
#         video.streams.get_highest_resolution().download()

# if __name__ == "__main__":
#     choice = input("Enter '1' to download a single video, '2' to download a playlist: ")

#     if choice == '1':
#         video_url = input("Enter the YouTube video URL: ")
#         download_youtube_video(video_url)
#     elif choice == '2':
#         playlist_url = input("Enter the YouTube playlist URL: ")
#         download_youtube_playlist(playlist_url)
#     else:
#         print("Invalid choice. Please enter '1' or '2'.")






import streamlit as st
import pytube
import tqdm
import os

def download_youtube_video(video_url, download_path):
    """Downloads a single YouTube video to the specified folder.

    Args:
        video_url: The URL of the YouTube video to download.
        download_path: The path where the video will be saved.
    """
    os.makedirs(download_path, exist_ok=True)
    os.chdir(download_path)
    video = pytube.YouTube(video_url)
    video.streams.get_highest_resolution().download()

def download_youtube_playlist(playlist_url, download_path):
    """Downloads a YouTube playlist to the specified folder.

    Args:
        playlist_url: The URL of the YouTube playlist to download.
        download_path: The path where the playlist will be saved.
    """
    os.makedirs(download_path, exist_ok=True)
    os.chdir(download_path)
    playlist = pytube.Playlist(playlist_url)
    for video in tqdm.tqdm(playlist.videos):
        video.streams.get_highest_resolution().download()

def main():
    st.title("YouTube Downloader")
    drive = st.selectbox("Select Drive to Store:", options=['C:', 'D:', 'E:', 'F:', 'G:'])
    folder_name = 'Hablu Progmmer javascript videos'
    download_path = os.path.join(drive, folder_name)

    choice = st.radio("Select an option:", ('Download a single video', 'Download a playlist', 'Show current path'))

    if choice == 'Download a single video':
        video_url = st.text_input("Enter the YouTube video URL:")
        if st.button("Download"):
            if video_url:
                download_youtube_video(video_url, download_path)
                st.success("Video downloaded successfully!")
            else:
                st.warning("Please enter a valid URL.")
    elif choice == 'Download a playlist':
        playlist_url = st.text_input("Enter the YouTube playlist URL:")
        if st.button("Download"):
            if playlist_url:
                download_youtube_playlist(playlist_url, download_path)
                st.success("Playlist downloaded successfully!")
            else:
                st.warning("Please enter a valid URL.")
    elif choice == 'Show current path':
        st.write(f"The files will be saved in: {download_path}")

if __name__ == "__main__":
    main()
