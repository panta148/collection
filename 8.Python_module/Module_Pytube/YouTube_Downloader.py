# this is the youtube video downloader app   
# i dont not got the any idea why this code is showing ther some error  

from tkinter import *
from pytube import YouTube
from functools import partial
def download(value):
    global text
    try:
        # url=https://www.youtube.com/watch?v=6L6XqWoS8tw
        yt=YouTube(url.get())
        # yt=YouTube('')
        a=yt.title
        # print(a)
        d=yt.streams.first()
        print(d)
        d.download()
        text.set("Download Completed!!")
    except KeyError as e:
        text.set("ERROR")
        print(e)



        
root=Tk()
root.title("..YouTube Video Downloader...")
root.resizable(0,0)
root.geometry('400x400')
root.config(bg="white")
l1=Label(root,text="Download Youtube Video",fg="white",bg="black",font="lucida 20 bold",padx=100,pady=10)
l1.pack(fill=X)
url=StringVar()
text=StringVar()
linkentry=Entry(root,textvariable=url,bg="#d1d1d1")
linkentry.place(x = 20,y = 60,width=350,height=40)
l2=Label(root,text="Past the Link Of The Video",fg="green",font="lucida 20 bold",padx=10,bg="white")
l2.place(x=20,y=120)
b=Button(root,text="Download",fg='white',bg="red",padx=10,pady=5,font="lucida 10 bold",command=partial(download,url))
b.place(x=150,y=200,width=100,height=50)
l3=Label(root,text="A",fg="green",bg="white",textvariable=text,font="lucida 15 bold",pady=10)
l3.place(x=50,y=300,width=300,height=50)
root.mainloop()
