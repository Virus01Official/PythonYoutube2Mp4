from pytube import YouTube

def download_video(link):
    try:
        youtube_object = YouTube(link)
        highest_resolution_stream = youtube_object.streams.get_highest_resolution()
        highest_resolution_stream.download()
        print("Download completed successfully.")
    except:
        print("An error occurred while downloading the video.")

if __name__ == "__main__":
    video_link = input("Enter the YouTube video URL: ")
    download_video(video_link)
