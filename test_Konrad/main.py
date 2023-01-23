from turtle import Turtle, Screen
import time
import random


screen = Screen()
screen.setup(width=400, height=400)
screen.listen()
            #turtle
turtle = Turtle()
colors = ["blue", "red", "black","gold","green"]
turtle.shape("turtle")
turtle.setheading(90)
turtle.penup()
turtle.setposition(0,-160)

cars = []
car_speed = 5
    #Create car ( and set a parameters )
for i in range(1,6):
        car = Turtle()
        car.shape("square")
        car.color(random.choice(colors))
        car.penup()
        # car.setposition(x=160, y=-100 + 25 * i)
        y_position = random.randint(-150, 150)
        car.goto(x=160, y=y_position)
        cars.append(car)




#set turtle to go up, and go back when it will be at the end
def go_up():
    turtle.forward(25)
    #print(turtle.position()[1])
    if turtle.position()[1] > 200 :
        turtle.setposition(0, -160)

screen.onkey(go_up , "Up")
game_on = True
while game_on:
    for car in cars:
        car.backward(5)
    time.sleep(0.3)



screen.exitonclick()