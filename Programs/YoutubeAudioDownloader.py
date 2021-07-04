# Testing Audio Work

from pytube import YouTube
import os

def lprint(L):
    for i in L:
        print(i)
            
print("Enter URL of Video")
link = input(": ")

video = YouTube(link)
streamqueryone = video.streams.filter(only_audio = True)
streamquerytwo = video.streams.filter(file_extension = 'mp4')
finalstreamquery = []

for i in streamqueryone:
    if streamquerytwo.count(i) == 0:
        try:
            finalstreamquery.append(i)
        except:
            pass
        
stream = finalstreamquery[-1]
stream.download(output_path = "/Users/joegr/Downloads")

print("Saved " + stream.title )