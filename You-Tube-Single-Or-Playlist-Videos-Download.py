import streamlit as st
import pytube
import tqdm
import os

def download_youtube_video(video_url):
    """Downloads a single YouTube video to the 'Hablu Progmmer javascript videos' folder.

    Args:
        video_url: The URL of the YouTube video to download.
    """
    # Create the 'Hablu Progmmer javascript videos' folder if it doesn't exist
    if not os.path.exists('Hablu Progmmer javascript videos'):
        os.makedirs('Hablu Progmmer javascript videos')
    
    # Change the working directory to the 'Hablu Progmmer javascript videos' folder
    os.chdir('Hablu Progmmer javascript videos')
    
    video = pytube.YouTube(video_url)
    video.streams.get_highest_resolution().download()

def download_youtube_playlist(playlist_url):
    """Downloads a YouTube playlist to the 'Hablu Progmmer javascript videos' folder.

    Args:
        playlist_url: The URL of the YouTube playlist to download.
    """
    # Create the 'Hablu Progmmer javascript videos' folder if it doesn't exist
    if not os.path.exists('Hablu Progmmer javascript videos'):
        os.makedirs('Hablu Progmmer javascript videos')
    
    # Change the working directory to the 'Hablu Progmmer javascript videos' folder
    os.chdir('Hablu Progmmer javascript videos')
    
    playlist = pytube.Playlist(playlist_url)
    for video in tqdm.tqdm(playlist.videos):
        video.streams.get_highest_resolution().download()

def main():
    st.title("YouTube Downloader")

    choice = st.radio("Select an option:", ('Download a single video', 'Download a playlist', 'Show current path'))

    if choice == 'Download a single video':
        video_url = st.text_input("Enter the YouTube video URL:")
        if st.button("Download"):
            if video_url:
                download_youtube_video(video_url)
                st.success("Video downloaded successfully!")
            else:
                st.warning("Please enter a valid URL.")
    elif choice == 'Download a playlist':
        playlist_url = st.text_input("Enter the YouTube playlist URL:")
        if st.button("Download"):
            if playlist_url:
                download_youtube_playlist(playlist_url)
                st.success("Playlist downloaded successfully!")
            else:
                st.warning("Please enter a valid URL.")
    elif choice == 'Show current path':
        current_path = os.getcwd()
        st.write(f"The files are being saved in: {current_path}")

if __name__ == "__main__":
    main()
