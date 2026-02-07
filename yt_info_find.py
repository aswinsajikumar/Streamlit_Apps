import streamlit as st
import yt_dlp

st.title("▶️ YouTube Video Info Finder")

url = st.text_input("Enter YouTube video URL")

def get_video_info(video_url):
    ydl_opts = {"quiet": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
    return info

if st.button("Get Video Info"):
    if url:
        try:
            info = get_video_info(url)

            st.subheader(info["title"])
            st.write("Channel:", info["uploader"])
            st.write("Duration:", info["duration"], "seconds")
            st.image(info["thumbnail"])

        except Exception as e:
            st.error("Invalid URL or unable to fetch video info")
    else:
        st.warning("Please enter a YouTube URL")
