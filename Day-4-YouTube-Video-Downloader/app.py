from pytube import YouTube
link = "https://www.youtube.com/watch?v=t8pPdKYpowI&t=11724s"
SAVE_PATH = r"C:\Users\Public\Downloads"
try: 
    # object creation using YouTube 
    yt = YouTube(link)
except: 
    print("Connection Error")

mp4_streams = yt.streams.filter(progressive=True,file_extension='mp4')

# get the video with the highest resolution
d_video = mp4_streams[-1]

try: 
    d_video.download(output_path=SAVE_PATH)
    print('▄▄▄▄▄▄▄▄▄▄▄▄ Video downloaded successfully! ▄▄▄▄▄▄▄▄▄▄▄▄')
    print(f'🚀 Find the video here {SAVE_PATH} on your PC 🚀')

except: 
    print("Some Error!")