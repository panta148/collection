'''pip install moviepy
pip install imageio'''
import imageio
import moviepy.editor
video=moviepy.editor.VideoFileClip('MyVideo.mp4')
audio=video.audio
audio.write_audiofile('MyVideo.mp3')
print("converted successfully")