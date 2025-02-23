from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- CONSTANTS ---------------------------------------- #
BG_COLOR = "#D1F8EF"
BLACK = "#000000"
ENTRY_COLOR = "#F8F3D9"
BUTTON_COLOR = "#A9B5DF"
BUTTON_BASIC = "#E8F9FF"
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- FINDER --------------------------------------------#
def find_password():
    website = website_text.get()
    try:
        with open("password.json","r",encoding="utf-8") as password_file:
            data = json.load(password_file)
        if website in data:
            mail = data[website]["mail"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {mail}\nPassword: {password}")
        else:
            messagebox.showwarning("Not Found","No Details About The Website")
    except (FileNotFoundError,json.JSONDecoder):
        messagebox.showwarning("Error","File Not Found Or Corrupted")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_text.delete(0,END)

    password_list = ([random.choice(letters) for _ in range(random.randint(6, 8))] +
    [random.choice(symbols) for _ in range(random.randint(2, 4))]+
    [random.choice(numbers) for _ in range(random.randint(2, 4))])

    random.shuffle(password_list)
    password = "".join(password_list)

    password_text.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------------ #
def save_password():
    website = website_text.get()
    mail = mail_text.get()
    password = password_text.get()
    new_data = {
        website : {
            "mail" : mail,
            "password" : password
        }
    }
    if len(website) == 0 or len(mail) == 0 or len(password) == 0:
        messagebox.showwarning("Empty Space", "Do Not Leave Any Field Empty !")
    else:
        confirm = messagebox.askyesno("Confirmation", "Do You Confirm?")

        if confirm:
            try:
                with open("password.json", "r+", encoding="utf-8") as file:
                    data = json.load(file)
            except (FileNotFoundError,json.JSONDecodeError) :
                data = {}

            data.update(new_data)
            with open("password.json", "w", encoding="utf-8") as file:
                json.dump(data, file,indent=4)

            website_text.delete(0, END)
            mail_text.delete(0,END)
            password_text.delete(0, END)
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
website_text.config(width=40,bg=ENTRY_COLOR)
website_text.grid(padx=5, pady=5, column=3, row=1)
website_text.focus()

mail_text = Entry()
mail_text.config(width=60,bg=ENTRY_COLOR)
mail_text.grid(padx=5, pady=5, column=3, row=2, columnspan=2)

password_text = Entry()
password_text.config(width=40,bg=ENTRY_COLOR)
password_text.grid(padx=5, pady=5, column=3, row=3)

# Buttons #
generate_password_button = Button(text="Generate Password", highlightthickness=0,
                                  command = lambda : password_generator())
generate_password_button.config(width=15,bg=BUTTON_BASIC,activebackground=BUTTON_COLOR)
generate_password_button.grid(padx=5, pady=5, column=4, row=3)

add_button = Button(text="Add", highlightthickness=0,
                    command= lambda : save_password())
add_button.config(width=52,bg=BUTTON_BASIC,activebackground=BUTTON_COLOR)
add_button.grid(padx=5, pady=5, column=3, row=5, columnspan=2)

find_button = Button(text="Search", highlightthickness=0,
                    command= lambda : find_password())
find_button.config(width=15,bg=BUTTON_BASIC,activebackground=BUTTON_COLOR)
find_button.grid(padx=5, pady=5, column=4, row=1)

window.mainloop()
