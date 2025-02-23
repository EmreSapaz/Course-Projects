from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- CONSTANTS ---------------------------------------- #
BG_COLOR = "#D1F8EF"
BLACK = "#000000"
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_text.delete(0,END)
    password_list_letter = [l for _ in range(random.randint(6,8)) for l in random.choice(letters)]
    password_list_symbol = [l for _ in range(random.randint(2, 4)) for l in random.choice(symbols)]
    password_list_number = [l for _ in range(random.randint(2, 4)) for l in random.choice(numbers)]
    password_list = password_list_number + password_list_symbol + password_list_letter
    random.shuffle(password_list)
    password = ""
    for i in password_list:
        password += i
    password_text.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------------ #
def save_password(x: Entry, y: Entry, z: Entry):
    if len(x.get()) == 0 or len(z.get()) == 0:
        messagebox.showwarning("Empty Space", "Do Not Leave Any Field Empty !")
    else:
        confirm = messagebox.askyesno("Confirmation", "Do You Confirm?")

        if confirm:
            with open("password.txt", "a+", encoding="utf-8") as file:
                file.write(f"{x.get()} | {y.get()} | {z.get()} \n")
            x.delete(0, END)
            z.delete(0, END)
# ---------------------------- UI SETUP ---------------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=BG_COLOR)
window.minsize(450, 300)

canvas = Canvas(width=200, height=200, highlightthickness=0, bg=BG_COLOR)
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(padx=5, pady=5, column=1, row=1, rowspan=3)

# Labels #
website_label = Label(text="Website                :", fg=BLACK, font="Arial", bg=BG_COLOR)
website_label.grid(padx=5, pady=5, column=2, row=1)

mail_label = Label(text="Email/Username :", fg=BLACK, font="Arial", bg=BG_COLOR)
mail_label.grid(padx=5, pady=5, column=2, row=2)

password_label = Label(text="Password            :", fg=BLACK, font="Arial", bg=BG_COLOR)
password_label.grid(padx=5, pady=5, column=2, row=3)

# Entry #
website_text = Entry()
website_text.config(width=60)
website_text.grid(padx=5, pady=5, column=3, row=1, columnspan=2)
website_text.focus()

mail_text = Entry()
mail_text.config(width=60)
mail_text.grid(padx=5, pady=5, column=3, row=2, columnspan=2)

password_text = Entry()
password_text.config(width=40)
password_text.grid(padx=5, pady=5, column=3, row=3)

# Buttons #
generate_password_button = Button(text="Generate Password", highlightthickness=0,
                                  command = lambda : password_generator())
generate_password_button.config(width=15)
generate_password_button.grid(padx=5, pady=5, column=4, row=3)

add_button = Button(text="Add", highlightthickness=0,
                    command=lambda: save_password(website_text, mail_text, password_text))
add_button.config(width=52)
add_button.grid(padx=5, pady=5, column=3, row=5, columnspan=2)

window.mainloop()
