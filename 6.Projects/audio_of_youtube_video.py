'''
pip install pafy
pip install youtube_dl
'''
import pafy
url=input('Enter url...\n->')
video=pafy.new(url)
# audiostreams=video.videostreams
audiostreams=video.audiostreams
print("starting.....")
for i in audiostreams:
    print(i.get_filesize())
audiostreams[3].download()    
print("Download Successfully")