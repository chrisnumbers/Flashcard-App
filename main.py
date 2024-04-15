import tkinter, pandas, time
BACKGROUNDCOLOR = "pink"


#Importing Data
def loadData():
    global data
    data = pandas.read_csv("data\spanish.csv",header=0)


#Random piece of data for flashcard
def newFlashcard():
    #languageLabel.config(text=data.columns.values[0].capitalize())
    canvas.itemconfig(languageName, text=data.columns.values[0].capitalize())
    randomData = data.sample()
    #wordLabel.config(text=randomData.values[0][0])
    canvas.itemconfig(word,text=randomData.values[0][0])
    canvas.itemconfig(flashcardImage, image=front)
    global translation
    translation =randomData.values[0][1]
    window.after(3000, flipCard)


def flipCard():
    global translation
    #languageLabel.config(text=data.columns.values[1].capitalize())
    #wordLabel.config(text=translation)
    canvas.itemconfig(languageName,text=data.columns.values[1].capitalize())
    canvas.itemconfig(word, text=translation)
    canvas.itemconfig(flashcardImage, image=back)
    #languageLabel.config(background="green")

#UI
window = tkinter.Tk()
window.config(padx=50,pady=50,background=BACKGROUNDCOLOR)
window.title("Flashcard App")
canvas = tkinter.Canvas(height=266,width=400, background=BACKGROUNDCOLOR,borderwidth=0,highlightthickness=0)
front = tkinter.PhotoImage(file="images\card_front.png")
back = tkinter.PhotoImage(file="images\card_back.png")
flashcardImage = canvas.create_image(200,133,image=front)
canvas.grid(row=0,column=0,columnspan=2)

checkmark = tkinter.PhotoImage(file="images\\right.png")
correct = tkinter.Button(image=checkmark, highlightthickness=0, borderwidth=0, background=BACKGROUNDCOLOR,activebackground=BACKGROUNDCOLOR,command=newFlashcard)
correct.grid(column=0,row=1)

xmark = tkinter.PhotoImage(file="images\wrong.png")
wrong = tkinter.Button(image=xmark, highlightthickness=0, borderwidth=0, background=BACKGROUNDCOLOR, activebackground=BACKGROUNDCOLOR,command=newFlashcard)
wrong.grid(column=1,row=1)

#languageLabel = tkinter.Label(font=("Arial", 24, "italic"),background="white")
languageName = canvas.create_text(200,60,font=("Arial", 24, "italic"))
#languageLabel.place(x=200,y=60, anchor="center")

#wordLabel = tkinter.Label(font=("Arial", 34),background="white",)
word = canvas.create_text(200,160,font=("Arial", 34))
#wordLabel.place(x=200,y=160,anchor="center")


loadData()
newFlashcard()

window.mainloop()