import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    email = email_un_input.get()
    password = password_input.get()

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs It OK to save?")
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
    else:
        if is_ok:
            with open("pass_gen.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, "end")
                password_input.delete(0, "end")
# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.config(padx=50, pady=50, bg="White")
window.title("Password Manager")
canvas = tk.Canvas(width=200, height=200, bg="white", highlightthickness=0)
bg_image = tk.PhotoImage(file="logo.png")
canvas.create_image(100,100,image=bg_image,)
canvas.grid(column=1,row=0)

########## LABEL ##########
website = tk.Label(text="Website: ",)
website.grid(column=0,row=1)
email_user_name = tk.Label(text="Email/username: ", bg="white")
email_user_name.grid(column=0, row=2)
password = tk.Label(text="Password", bg="white")
password.grid(column=0, row=3)

########## Input Field ##########
website_input = tk.Entry(width=35, bg="white")
website_input.grid(column=1, row=1, columnspan=2)
email_un_input = tk.Entry(width=35, bg="white")
email_un_input.grid(column=1, row=2, columnspan=2)
email_un_input.insert(0, "fulanito@gmail.com")
password_input = tk.Entry(width=21, bg="white")
password_input.grid(column=1,row=3)

########## Buttons ##########
generate_pw = tk.Button(text="Generate Password", bg="white", command=generate_password)
generate_pw.grid(column=2, row=3)
add = tk.Button(text="Add", width=36, bg="white", command=save)
add.grid(column=1, row=4,columnspan=2)

window.mainloop()



