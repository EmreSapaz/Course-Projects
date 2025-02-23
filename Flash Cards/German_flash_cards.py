from tkinter import *
from tkinter import PhotoImage
import random
import pandas

# --------------------------- CONSTANTS -------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
BLACK = "#000000"

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("words.csv")

dictionary = data.to_dict(orient="records")
current_card = {}
# --------------------------- NEXT CARD -------------------------------- #
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(dictionary)
    canvas.itemconfig(canvas_background,image=card_front)
    canvas.itemconfig(title_canvas,text="German",fill="black")
    canvas.itemconfig(word_canvas, text=current_card["German"],fill="black")
    flip_timer = window.after(3000, func=flip_card)
# --------------------------- TURN THE CARD ---------------------------- #
def flip_card():
    global current_card
    canvas.itemconfig(canvas_background,image=card_back)
    canvas.itemconfig(title_canvas,text="English",fill="white")
    canvas.itemconfig(word_canvas,text=current_card["English"],fill="white")
# --------------------------- DISCARD CARD ----------------------------- #
def discard_card():
    global current_card
    dictionary.remove(current_card)
    learn_data = pandas.DataFrame(dictionary)
    learn_data.to_csv("words_to_learn.csv",index=False)
    next_card()
# --------------------------- UI SETUP --------------------------------- #
window = Tk()
window.title("Flash Cards")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)
# --------------------------- IMAGES ----------------------------------- #
card_back = PhotoImage(file="card_back.png")
card_front = PhotoImage(file="card_front.png")

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
canvas_background = canvas.create_image(400,263,image = card_front)
canvas.grid(column=1,row=1,columnspan=3)
title_canvas = canvas.create_text(400, 150 ,text="Title",font=("Ariel",40,"italic"))
word_canvas = canvas.create_text(400,263,text="Word",font=("Ariel",60,"bold"))

# --------------------------- BUTTONS ---------------------------------- #
right_image = PhotoImage(file="right.png")
right_button = Button(image = right_image,highlightthickness=0,highlightcolor=BACKGROUND_COLOR,
                      command= discard_card)
right_button.config(bg=BACKGROUND_COLOR)
right_button.grid(column=3,row=2)

wrong_image = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_image,highlightthickness=0,highlightcolor=BACKGROUND_COLOR,
                      command= next_card)
wrong_button.config(bg=BACKGROUND_COLOR)
wrong_button.grid(column=1,row=2)

next_card()

window.mainloop()