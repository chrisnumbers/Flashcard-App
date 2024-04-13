import tkinter

BACKGROUNDCOLOR = "gray"


#UI

window = tkinter.Tk()
window.config(padx=50,pady=50,background=BACKGROUNDCOLOR)
window.title("Flashcard App")
canvas = tkinter.Canvas(height=266,width=400, background=BACKGROUNDCOLOR,borderwidth=0,highlightthickness=0)
front = tkinter.PhotoImage(file="images\card_front.png")
canvas.create_image(200,133,image=front)
canvas.grid(row=0,column=0,columnspan=2)

checkmark = tkinter.PhotoImage(file="images\\right.png")
correct = tkinter.Button(image=checkmark, highlightthickness=0, borderwidth=0, background=BACKGROUNDCOLOR)
correct.grid(column=0,row=1)

xmark = tkinter.PhotoImage(file="images\wrong.png")
wrong = tkinter.Button(image=xmark, highlightthickness=0, borderwidth=0, background=BACKGROUNDCOLOR)
wrong.grid(column=1,row=1)

#Current-Language
language = "Spanish"
languageLabel = tkinter.Label(text=language, font=("Arial", 30),background="white")
#languageLabel.config(justify="center")
languageLabel.place(x=200,y=60, anchor="center")


#Word to be Translated



window.mainloop()