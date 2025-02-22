from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
LIGHT_BLUE = "#A9B5DF"
LILA = "#EABDE6"
BLACK = "#000000"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPS
    window.after_cancel(timer)
    pomodoro_tick.config(text="")
    timer_label.config(text="Timer",fg=BLACK)
    canvas.itemconfig(timer_text,text="00 : 00")
    REPS = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Break",fg=PINK)
    elif REPS % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break",fg=RED)
    else:
        countdown(work_sec)
        timer_label.config(text="Study",fg=BLACK)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min} : {count_sec}")
    if count >= 0:
        global timer
        timer = window.after(1000,countdown,count - 1)
    else:
        start_timer()
        if REPS % 2 == 0:
            pomodoro_tick.config(text="✓" * int(REPS / 2))
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(bg=LIGHT_BLUE)
window.minsize(600,450)

timer_label = Label(text="Timer",fg=BLACK,font=("Arial",30,"bold"),bg=LIGHT_BLUE)
timer_label.place(x=240,y=50)

canvas = Canvas(width=450,height=150,bg=LIGHT_BLUE,highlightthickness = 0 )
clock = PhotoImage(file="digital_clock.png")
canvas.create_image(225,75,image = clock)
timer_text = canvas.create_text(225,75,text="00 : 00",font=("Arial",30,"bold"),fill = "black")
canvas.place(x=75,y=150)

start_button = Button(text="Start", activebackground=LILA, bg=LIGHT_BLUE, highlightthickness=0,
                      font=("Times New Roman", 20, "bold"),command=start_timer)
start_button.place(x=112, y=375)

reset_button = Button(text="Reset", activebackground=LILA, bg=LIGHT_BLUE, highlightthickness=0,
                      font=("Times New Roman", 20, "bold"),command=reset_timer)
reset_button.place(x=412, y=375)

pomodoro_tick = Label(fg=GREEN,font=("Arial",20,"bold"),bg=LIGHT_BLUE)
pomodoro_tick.place(x=230,y=325)

window.mainloop()

