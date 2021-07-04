# Testing Work

from pytube import YouTube

print("Enter URL of Video")
link = input(": ")

video = YouTube(link)
stream = video.streams.get_highest_resolution()

stream.download("/Users/joegr/Downloads")
print("Saved " + stream.title)