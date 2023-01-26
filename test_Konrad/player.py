from turtle import  Turtle, Screen
START = (-150, 0)
END_LINE = 280
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setposition(START)
        self.color("black")



screen = Screen()
screen.exitonclick()