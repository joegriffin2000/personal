# Testing Work

from pytube import YouTube
import os
userName = os.getlogin()

print("Enter URL of Video")
link = input(": ")

video = YouTube(link)
print(video.title())
#stream = video.streams.get_highest_resolution()

#stream.download("/Users/"+userName+"/Downloads")
#print("Saved " + stream.title)
