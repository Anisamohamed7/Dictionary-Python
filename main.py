from tkinter import *
import json
from difflib import get_close_matches
from tkinter import messagebox
import pyttsx3

engine = pyttsx3.init() #Creating instance of engine class
voice=engine.getProperty("voices")
engine.setProperty("voice", voice[0].id)

#Functionality
def search():
    data =json.load(open("data.json"))
    word = enterwordEntry.get()
    word=word.lower()
    if word in data:
        meaning =data[word]
        textarea.delete(1.0, END)
        for item in meaning:
            textarea.insert(END,u'\u2022' +item+"\n\n")
    elif len(get_close_matches(word, data.keys()))>0:
        close_match = get_close_matches(word, data.keys())[0]
        res = messagebox.askyesno("Confirm", f'Did you mean {close_match} instead?')
        if res ==True:
            enterwordEntry.delete(0,END)
            enterwordEntry.insert(END, close_match)
            meaning = data[close_match]
            textarea.delete(1.0, END)
            for item in meaning:
                textarea.insert(END, u'\u2022' + item + "\n\n")

        else:
            messagebox.showerror("Error", "The word does not exist. Please double check it.")
            enterwordEntry.delete(0, END)
            textarea.delete(1.0, END)
    else:
        messagebox.showinfo("Information", "The word does not exist")
        enterwordEntry.delete(0, END)
        textarea.delete(1.0, END)

#Clear
def clear():
    enterwordEntry.delete(0, END)
    textarea.delete(1.0, END)

#exit
def exit():
    res =messagebox.askyesno("Confirm", "Do you want to exit?")
    if res == True:
        root.destroy()
    else:
        pass

#Audio
def wordaudio():
    engine.say(enterwordEntry.get())
    engine.runAndWait()

def meaningaudio():
    engine.say(textarea.get(1.0, END))
    engine.runAndWait()

#GUI
root = Tk()
root.geometry("1000x626+100+30")
root.title("Anisa's dictionary")
root.resizable(0,0)
bgimage= PhotoImage(file="wallpaper2.png")
bgLabel=Label(root, image=bgimage)
bgLabel.place(x=0,y=0)
enterwordlabel=Label(root, text="ENTER WORD", font=("arial",20,"bold"),bg="seashell1")
enterwordlabel.place(x=530, y=20)

enterwordEntry=Entry(root, font=("arial", 15), justify="center", bd=5, relief ="groove")
enterwordEntry.place(x=510,y=80)
searchimage=PhotoImage(file="search (2).png")
searchButton=Button(root,image=searchimage,bd=0, bg="seashell1", cursor="hand2", activebackground="seashell1", command=search)
searchButton.place(x=580, y=150)

micimage=PhotoImage(file="microphone-black-shape.png")
micButton=Button(root, image=micimage,bd=0, bg="seashell1", cursor="hand2",
                 activebackground="seashell1", command =wordaudio)
micButton.place(x=660, y=150)

meaninglabel=Label(root, text="MEANING", font=("arial",29,"bold"),bg="seashell1")
meaninglabel.place(x=530, y=240)
textarea=Text(root, width=35, height=6,font=("arial",14), bd=8, relief="groove")
textarea.place(x=400, y=300)

audioimage=PhotoImage(file="speaker-filled-audio-tool.png")
audioButton = Button(root, image=audioimage, bd=0, bg="seashell1",cursor="hand2",
                     activebackground="seashell1", command=meaningaudio)
audioButton.place(x=500, y=500)

clearimage=PhotoImage(file="clear.png")
clearButton = Button(root, image=clearimage, bd=0, bg="seashell1",cursor="hand2",
                     activebackground="seashell1", command=clear)
clearButton.place(x=610, y=500)

exitimage=PhotoImage(file="logout.png")
exitButton = Button(root, image=exitimage, bd=0, bg="seashell1",cursor="hand2", activebackground="seashell1", command=exit)
exitButton.place(x=720, y=500)

def enter_function(event):
    searchButton.invoke()

root.bind('<Return>', enter_function)
root.mainloop()