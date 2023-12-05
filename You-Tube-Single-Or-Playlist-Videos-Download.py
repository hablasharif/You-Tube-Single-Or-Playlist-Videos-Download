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
    os.chdir(download_path)
    video = pytube.YouTube(video_url)
    video.streams.get_highest_resolution().download()

def download_youtube_playlist(playlist_url, download_path):
    """Downloads a YouTube playlist to the specified folder.

    Args:
        playlist_url: The URL of the YouTube playlist to download.
        download_path: The path where the playlist will be saved.
    """
    os.chdir(download_path)
    playlist = pytube.Playlist(playlist_url)
    for video in tqdm.tqdm(playlist.videos):
        video.streams.get_highest_resolution().download()

def main():
    st.title("YouTube Downloader")
    drive = st.selectbox("Select Drive to Store:", options=['C:', 'D:', 'E:', 'F:', 'G:'])
    download_path = os.path.join(drive, 'Hablu Progmmer javascript videos')

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
