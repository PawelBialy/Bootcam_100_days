from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import  pyperclip
import json

GREEN = "#9bdeac"
PINK = "#e2979c"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_letters + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = webside_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_dictionary = {
        website:{
            "email": email,
            "password": password
        }
    }


    if len(website) ==0 or len(password) ==0:
        messagebox.showinfo(title="Hey!", message="Text field can't be empty.")
    else:
        with open("save_data.json", "r") as data_file:
            # Reading old data
            data= json.load(data_file)
            #Updating old data with new data
            data.update(new_dictionary)
        with open("save_data.json","w") as data_file:
            #saving updated data
            json.dump(data, data_file, indent=4)

            webside_entry.delete(0, END)
            password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
# window.minsize(width=300,height=200)
window.config(padx=50,pady=50, )

canvas = Canvas(width=200, height=200,highlightthickness=0, )
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=padlock_img)
canvas.grid(column=1, row=0)

webside_text = Label(text="Webside:",)
webside_text.grid(column=0, row=1)

email_text = Label(text="Email/Username:")
email_text.grid(column=0,row=2)

password_text = Label(text="Password:")
password_text.grid(column=0, row=3)

webside_entry = Entry(width=50,)
webside_entry.grid(column=1,row=1, columnspan=2)
webside_entry.focus()

email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0,"adres_email@gmail.com")

password_entry = Entry(width=32, )
password_entry.grid(column=1, row=3, columnspan=1)


new_password = Button(text="Random Password", command=generate_password )
new_password.grid(column=2,row=3, columnspan=1)

add_button = Button(width=43, text="Add",command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()