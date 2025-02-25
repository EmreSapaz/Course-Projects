from tkinter import *
from tkinter import PhotoImage
from questions import question_answer_pair
import random

BG_COLOR = "#27667B"
SCREEN_COLOR = "#F2EFE7"
num_of_questions = 0
question = question_answer_pair[num_of_questions][0]
answer = question_answer_pair[num_of_questions][1]
SCORE : int = 0
length = len(question_answer_pair)
# ---------------------------------- NEXT QUESTION ----------------------- #
def next_question():
    global answer,question,num_of_questions
    if num_of_questions + 1 < length:
        true_button.config(state="active")
        false_button.config(state="active")
        canvas.config(bg=SCREEN_COLOR)
        num_of_questions += 1
        new_question = question_answer_pair[num_of_questions][0]
        new_answer = question_answer_pair[num_of_questions][1]
        answer = new_answer
        canvas.itemconfig(question_text,text=f"{new_question}")

    else:
        canvas.config(bg=SCREEN_COLOR)
        canvas.itemconfig(question_text,text="You Reached the End of the Quiz\n                  Thank you")
# --------------------------------- BUTTON FUNCTIONS --------------------- #
def right():
    global SCORE
    if answer == "True" :
        SCORE += 1
        canvas.config(bg="green")
        score.config(text=f"Score : {SCORE}")
        true_button.config(state="disabled")
        false_button.config(state="disabled")
    else:
        canvas.config(bg="red")
        true_button.config(state="disabled")
        false_button.config(state="disabled")
    window.after(1000,next_question)


def wrong():
    global SCORE
    if answer == "False" :
        SCORE += 1
        canvas.config(bg="green")
        score.config(text=f"Score : {SCORE}")
        true_button.config(state="disabled")
        false_button.config(state="disabled")
    else:
        canvas.config(bg="red")
        true_button.config(state="disabled")
        false_button.config(state="disabled")
    window.after(1000,next_question)
# ---------------------------------- UI ---------------------------------- #
window = Tk()
window.title("Quiz")
window.config(padx= 20, pady= 20, bg=BG_COLOR)

#Canvas#
canvas = Canvas(width=450,height=300,highlightthickness=0,bg=SCREEN_COLOR)
canvas.grid(column= 1, row= 2, columnspan= 2, pady=25)
question_text = canvas.create_text(225,150,width=445,text=f"{question}",font=("Arial",20,"italic"))

#Label#
score = Label(text=f"Score : {SCORE}",font=("Arial",20,"italic"),fg="white")
score.config(bg=BG_COLOR)
score.grid(column= 1, row= 1, columnspan= 2)

#Buttons#
true_image = PhotoImage(file="true.png")
true_button = Button(image=true_image,command= lambda : right())
true_button.config(bg=BG_COLOR)
true_button.grid(column= 1, row= 3)

false_image = PhotoImage(file="false.png")
false_button = Button(image=false_image,command= lambda : wrong())
false_button.config(bg=BG_COLOR)
false_button.grid(column= 2, row= 3)

window.mainloop()