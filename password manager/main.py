from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_number = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter + password_number + password_symbol
    random.shuffle(password_list)
    generated = "".join(password_list)
    password_entry.insert(0,generated)
    pyperclip.copy(generated)

#------------------------------SEARCH BUTTON-------------------------------------#
def find_password():
    entry= website_entry.get()
    try:
        with open("data.json") as data:
            datas = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Website not found", message="The Website you entered doesn't seem to exist")
    else:
        if entry in datas:
            email=datas[entry]["email"]
            passwd = datas[entry]["password"]
            messagebox.showinfo(title="Information found",
                                message=f"The entered information is:\n\nEmail: {email}\nPassword: {passwd}")
        else:
            messagebox.showinfo(title="Website not found", message="The Website you entered doesn't seem to exist")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def on_add():

    web = website_entry.get()
    emails=email_entry.get()
    passwrd = password_entry.get()
    new_data = {
        web:{
            "email": emails,
            "password": passwrd
        }
    }

    if web=="" or emails=="" or passwrd=="":
        messagebox.showinfo(title="INVALID", message="You cannot leave fields empty.  Please fill it up")
    else:
        try:
            with open("data.json", "r") as data:
                new_datas = json.load(data)

        except FileNotFoundError:
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)
        else:
            new_datas.update(new_data)
            with open("data.json", "w") as data:
                json.dump(new_datas, data, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png" )
canvas.create_image( 100, 100, image = img)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0)
email = Label(text="Email/Username:")
email.grid(row=2, column=0)
password = Label(text="Password:")
password.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1,columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1,columnspan=2)
email_entry.insert(0,"somename@email.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2)

generate_button = Button(text="Generate Password", command= generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add",width=36, command=on_add)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search",width=15, command=find_password)
search_button.grid(row=1,column=2)

window.mainloop()