from  tkinter import *

def button_click():
    miles = float(input.get())
    km = miles * 1.609
    result.config(text=f"{km}")



window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=180, height=100)
window.config(padx=20,pady=20)

# empty= Label(text="_")
# empty.grid(column=0,row=0)

input=Entry(width=10)
input.grid(column=1,row=0)

miles = Label(text="Miles")
miles.grid(column=2,row=0)

equal = Label(text="is equal to ")
equal.grid(column=0,row=1)

result = Label(text="0")
# result.config(text=input.get())
result.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2,row=1)



calculate = Button(text="Calculate", command=button_click)
calculate.grid(column=1,row=2)
# def button_click():
#     print("I got clicked")
#     new_text = input.get()
#     my_label.config(text=new_text)
#
# window = Tk()
# window.title("My firts GUI Program")
# window.minsize(width=500,height=300)
# window.config(padx=20,pady=20)
# #Label
# my_label = Label(text="Create it in the middle",font=("Arial",24,"bold"))
# my_label.config(text="New text")
# my_label.grid(column=0,row=0)
# my_label.config(padx=50, pady=50)
# #Button
# button = Button(text="Click me", command=button_click)
# button.grid(column=1,row=1)
#
# #New button
# new_button = Button(text="That's new button", command=button_click )
# new_button.grid(column=2, row=0)
#
#
# #Entry
# input = Entry(width=10)
# print(input.get())
# input.grid(column=3,row=2)
#
#
#
window.mainloop()
