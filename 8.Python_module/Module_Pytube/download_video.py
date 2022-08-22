# from pytube import YouTube
# yt=YouTube('https://www.youtube.com/watch?v=xhNwhL58c9')
# yt.title
from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=xhNwhL58c9E')
a=yt.thumbnail_url
print("The thumbnail of the video is \n",a)
title=yt.title
print("The title of the video is\n",title)
c=yt.streams.all()
for i in c:
    print(i,"\n")
print("Thanks you man")   
d=yt.streams.first()
print(d) 
d.download()
print("The download finished man, lets enjoy it")