from tkinter import *
from pytube import YouTube

root = Tk()

a = 0


def video():
    print("Загружаю видео...")
    video_name = (f"{name}.mp4")
    yt.streams.get_highest_resolution().download(video_name)
    print("Загрузка видео успешно завершена!")


def audio():
    print("Загружаю аудиофайл...")
    audio_name = (f"{name}.mp3")
    yt.streams.filter(only_audio=True).first().download(audio_name)
    print("Загрузка аудиофайла успешно завершена!")


def doneling():
        global a
        if a <= 0:
        	a += 1
        	yt = YouTube(video_link.get())
        	name = yt.title()
        	info = Label(frame, text=(f'Название видео:{name}'), bg='green',bd=0, font=40)
        	info.pack()
        	btn2 = Button(frame, bg='fuchsia', fg='yellow',  text="Скачать видео", command=video)
        	btn2.pack()
        	btn3 = Button(frame, bg='fuchsia', fg='yellow',  text="Скачать аудио", command=audio)
        	btn3.pack()
        else:
        	err = Label(frame, relx=0.2, rely=0.5, relwidth=0.3, relheight=0.3)

width = '50'
height = '40'

root['bg'] = 'violet'
root.title('СКАЧИВАТЕЛЬ ВИДЕО С ЮТУБА')
root.geometry(f'{width}x{height}')
root.resizable(width=False, height=False)

frame = Frame(root, bg='purple', bd=1)
frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)


video_link = Entry(frame, text='Введите ссылку на видео: ', bg='pink', font=50)
video_link.pack()

btn1 = Button(frame, bg='fuchsia', fg='yellow',  text="Найти видео", command=doneling)
btn1.pack()

root.mainloop()
