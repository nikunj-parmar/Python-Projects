from tkinter import *
from pytube import YouTube

# display window
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Youtube video downloader")

Label(root,text = 'YT Video Downloader', font ='arial 20 bold').pack()
link = StringVar()
Label(root, text = 'Insert Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 52, y = 90)

# for start the downloading
def Download():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'Your Video has been downloaded!', font = 'arial 15').place(x= 180 , y = 210)  

Button(root,text = 'DOWNLOAD', font = 'arial 13 bold' ,bg = 'white', padx = 2, command = Download).place(x=180 ,y = 150)
root.mainloop()