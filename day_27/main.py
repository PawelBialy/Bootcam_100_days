from  tkinter import *

def button_click():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My firts GUI Program")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)
#Label
my_label = Label(text="Create it in the middle",font=("Arial",24,"bold"))
my_label.config(text="New text")
my_label.grid(column=0,row=0)
my_label.config(padx=50, pady=50)
#Button
button = Button(text="Click me", command=button_click)
button.grid(column=1,row=1)

#New button
new_button = Button(text="That's new button", command=button_click )
new_button.grid(column=2, row=0)


#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3,row=2)



window.mainloop()
