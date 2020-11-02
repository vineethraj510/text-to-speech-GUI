import tkinter
from tkinter import filedialog as f
import pyttsx3  # text to speech conversion library(it works offline)
from PIL.ImageTk import PhotoImage
from PIL import Image

engine = pyttsx3.init()
screen = tkinter.Tk()
screen.title('Text to Speech Conversion GUI')
screen.geometry('600x450')
screen.configure(background='black')
photo = PhotoImage(Image.open("ts.jpg").resize((590, 290)))
lab = tkinter.Label(screen, image = photo)
lab.pack()



def Btn_click():
    s = f.askopenfile(initialdir = '/Desktop',filetypes = (("Text files","*.txt"),("PDF File","*.pdf*")))
    file = s.name


    with open(file,'r') as g:
        info = g.read()
        voices = engine.getProperty('voices')
        a.setProperty("language",'hi')
        engine.setProperty("rate", 100) # speed of voice
        engine.setProperty('voice', voices[1].id)  # to set voice 

        engine.say(info)
        engine.save_to_file(info,'tttttt.mp3')

        engine.runAndWait()


def scren_close():
    screen.destroy()




label = tkinter.Label(screen, text = 'Please Upload your Text and I will Read it for you',padx = 5,pady = 5,
    background = 'black', foreground = 'white',font = ('Times new Roman',14))
label.pack()

Button = tkinter.Button(screen, text = 'Search for the Text', command = Btn_click,padx = 1,pady = 1,background = 'blue', foreground = 'white',font = ('Times new Roman',14) )
Button.pack()


Button2 = tkinter.Button(screen, text = 'Stop Reading and Close Window', command = scren_close,padx = 1,pady = 1,background = 'blue', foreground = 'white',font = ('Times new Roman',14) )
Button2.pack()

screen.mainloop()


