import tkinter
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    check = 0
    check += 1
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(6, 9))]
    password_symbols = [choice(symbols) for _ in range(randint(3, 5))]
    password_numbers = [choice(numbers) for _ in range(randint(3, 5))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    if check >= 1:
        entry_password.delete(0, tkinter.END)
        entry_password.insert(0,password)
        pyperclip.copy(password)
    else:
        entry_password.insert(0, password)
        pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website:{
            "email":email,
            "password":password
    }
    }
    if len(website) <=0 or len(password) <= 0 or len(email) <= 10:
        messagebox.showinfo(title="Oops!", message="Empty fields are not allowed!")
    else:
        try:
            with open("data.json","r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            entry_email.delete(0, len(email) - 10)
            entry_website.delete(0, tkinter.END)
            entry_password.delete(0, tkinter.END)

# ---------------------------- FIND PASSWORD (SEARCH) ------------------------------- #
def find_password():
    website = entry_website.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error!", message="File Not Found!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
            entry_website.delete(0, tkinter.END)
        else:
            messagebox.showerror(title="Error!", message=f"There Is No Details for {website} Exist!")
            entry_website.delete(0, tkinter.END)

# ---------------------------- UI SETUP ------------------------------- #
# Window
window = tkinter.Tk()
window.title("Password Manger")
window.config(padx=50, pady=50)
# Image
canvas = tkinter.Canvas(width=200, height=200)
image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)
# label website
label_website = tkinter.Label(text="Website:")
label_website.grid(column=0,row=2)
# label Email/Username
label_email = tkinter.Label(text="Email/UserName:")
label_email.grid(column=0,row=3)
# label password
label_password = tkinter.Label(text="Password:")
label_password.grid(column=0,row=4)
# entry website
entry_website = tkinter.Entry(width=36)
entry_website.grid(row=2, column=1, columnspan=2)
entry_website.focus()
# entry email
entry_email = tkinter.Entry(width=36)
entry_email.grid(row=3,column=1, columnspan=2)
entry_email.insert(0, "@gmail.com")
# entry email
entry_password = tkinter.Entry(width=36)
entry_password.grid(row=4, column=1, columnspan=2)
# generate password Button
button_password = tkinter.Button(text="Generate",width=30, command=generate_password)
button_password.grid(row=5, column=1, columnspan=2)
# # Add Button
add_button = tkinter.Button(text="Add", width=30,command=save)
add_button.grid(row=6, column=1, columnspan=2)
# search Button
search_button = tkinter.Button(text="Search", width=30, command=find_password)
search_button.grid(row=1, column=1, columnspan=2)

window.mainloop()