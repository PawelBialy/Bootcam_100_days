from  tkinter import *

window = Tk()

window.title("My firts GUI Program")
window.minsize(width=500,height=300)

my_label = Label(text="Create it in the middle",font=("Arial",24,"bold"))
my_label.pack()

my_label.config(text="New text")

#button
def button_click():
    # optional
    new_text = input.get()
    my_label.config(text=new_text)

    # my_label.config(text=input.get()) --> This is also  working, and for me is simpler.

button = Button(text="Click me", command=button_click)
button.pack()

#Entry

input = Entry(width=10)
input.pack()
# input.get()

#
# def add (*args):
#     for n in args:
#         print(n)
#
# add(3,5,7,9)


window.mainloop()
