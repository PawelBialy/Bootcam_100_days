import turtle
from turtle import Turtle


screen = turtle.Screen()

screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


answer_satate = screen.textinput("Guess the State", prompt="What is another state's name? ")
print(answer_satate)


turtle.mainloop()
screen.exitonclick()