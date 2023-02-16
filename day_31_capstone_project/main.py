from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800,height=526)
card_front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263,image= card_front_image)
canvas.create_text(400,150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="Word" , font=("Ariel", 50, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)



wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image,)
wrong_button.grid(row=1, column=0, )

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, )
right_button.grid(row=1, column=1)




window.mainloop()









window.mainloop()












