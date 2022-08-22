from pytube import YouTube
yt=YouTube('https://www.youtube.com/watch?v=yWZx0c45Yx8')
a=yt.streams.filter(progressive=True).all()
print(a)