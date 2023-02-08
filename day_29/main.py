from tkinter import *
GREEN = "#9bdeac"
PINK = "#e2979c"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(width=300,height=200)
window.config(padx=20,pady=20, )

canvas = Canvas(width=200, height=200,highlightthickness=0, )
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=padlock_img)
canvas.pack()






window.mainloop()