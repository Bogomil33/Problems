#write a script that downloads a song from youtube, a pic from random site and generates a video using the song and the image as input. 
#installed pytube
#installed google_images_download
#installed ffmpeg

from pytube import YouTube
from google_images_download import google_images_download
import yt_dlp
import moviepy.editor as mpe
import requests

#audio download part
video_url = 'https://www.youtube.com/watch?v=qf_8dyLdT5s'

ydl_opts = {
    'format': 'bestaudio/best',
    'ffmpeg_location': 'C:/ffmpeg-master-latest-win64-gpl/bin',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': 'C:/Users/radu0/Downloads/yt/firstSong',
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    print("Audio downloaded successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

{
#image download from google search querry part
# response = google_images_download.googleimagesdownload()
# search_queries = 'ugly monkey'
#
# def downloadimages(query):
#     # keywords is the search query
#     # format is the image file format
#     # limit is the number of images to be downloaded
#     # print urls is to print the image file url
#     # size is the image size which can
#     # be specified manually ("large, medium, icon")
#     # aspect ratio denotes the height width ratio
#     # of images to download. ("tall, square, wide, panoramic")
#     arguments = {"keywords": query,
#                  #"format": "jpg",
#                  "limit": 4,
#                  "print_urls": True,
#                  #"size": "medium",
#                  #"aspect_ratio": "panoramic",
#                  "output_directory": 'C:/Users/radu0/Downloads/yt'}
#     try:
#         response.download(arguments)
#
#     # Handling File NotFound Error
#     except FileNotFoundError:
#         arguments = {"keywords": query,
#                      "format": "jpg",
#                      "limit": 1,
#                      "print_urls": True,
#                      "size": "medium"}
#
#
# downloadimages(search_queries)
}
#using requests
url = 'https://tse1.mm.bing.net/th?q=pictures%20of%20a%20ugly%20monkey&w=474&h=274&c=7'
response = requests.get(url, stream=True)
if response.status_code == 200:
    with open("C:/Users/radu0/Downloads/yt/uglyM.jpg", 'wb') as f:
        f.write(response.content)

#making final music video
#my_clip = mpe.VideoFileClip('C:/Users/radu0/Downloads/yt/uglyM.jpg')
my_clip = mpe.ImageClip('C:/Users/radu0/Downloads/yt/uglyM.jpg', duration=120)
audio_background = mpe.AudioFileClip('C:/Users/radu0/Downloads/yt/firstSong.mp3')

final = my_clip.set_audio(audio_background)
final.write_videofile("C:/Users/radu0/Downloads/yt/ClassicalMusic.mp4", fps=24)
