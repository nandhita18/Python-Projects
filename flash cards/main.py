from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#FFFFFF"

#-----------------------FLASHING CARDS-------------------#
pd=pandas.read_csv("data/french_words.csv")
to_learn= pd.to_dict(orient="records")
current_card={}

def random_word():
        global current_card
        current_card = random.choice(to_learn)
        Canvas.itemconfig(card_title, text="French")
        Canvas.itemconfig(card_word, text=current_card["French"])
        Canvas.itemconfig(card_bg, image= img)

def flashing_newcard():
        Canvas.itemconfig(card_title, text="English", fill= "white")
        Canvas.itemconfig(card_word, text=current_card["English"], fill="white")
        Canvas.itemconfig(card_bg, image=new_img)

#------------------------UI INTERFACE---------------------#
window=Tk()
window.title("Flash card")
window.config(pady=50, padx=50,bg=BACKGROUND_COLOR)

window.after(3000, flashing_newcard())

canvas=Canvas(width=800, height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
img = PhotoImage(file="images/card_front.png")
new_img = PhotoImage(file="images/card_back.png")
card_bg=canvas.create_image(400,263, image= img)
card_title = canvas.create_text(400,150, text="", font=("Ariel", 48, "italic"))
card_word = canvas.create_text(400,263,text="", font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0, columnspan=2)

left_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=left_img,highlightthickness=0, command=random_word)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button=Button(image= right_img, highlightthickness=0, command=random_word)
right_button.grid(row=1,column=1)

random_word()


window.mainloop()