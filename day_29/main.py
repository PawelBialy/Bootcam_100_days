from tkinter import *
GREEN = "#9bdeac"
PINK = "#e2979c"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3, columnspan=1)

new_password = Button(text="Random Password", )
new_password.grid(column=2,row=3, columnspan=1)

add_button = Button(width=43, text="Add")
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()