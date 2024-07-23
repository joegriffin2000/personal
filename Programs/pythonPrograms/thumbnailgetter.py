# Testing
# 

from pytube import YouTube
import os
userName = os.getlogin()

print("Enter URL of Video")
link = input(": ")

video = YouTube(link)

print(video.thumbnail_url())
