from turtle import Turtle, Screen
import time
import random


screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
turtle = Turtle()
level = 1

            #my turtle

turtle.penup()
turtle.shape("turtle")
turtle.setheading(90)
turtle.setposition(0,-275)

colors = ["blue", "red", "black","gold","green"]
cars = []
car_move = 5

    #Create car ( and set a parameters )
def new_car():
    random_car_number = random.randint(1,6)
    if random_car_number == 2:
        car = Turtle("square")
        car.hideturtle()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.color(random.choice(colors))
        car.setposition(x=160, y=-100 + 20)
        y_position = random.randint(-245, 245)
        car.goto(x=280, y=y_position)
        car.showturtle()
        cars.append(car)


#set turtle to go up, and go back when it will be at the end
def go_up():
    global level
    turtle.forward(25)
    #print(turtle.position()[1])
    if turtle.position()[1] > 300 :
        level += 1
        global car_move
        turtle.hideturtle()
        turtle.goto(0, -270)
        turtle.showturtle()
        #here to be level
        car_move += 5


screen.listen()
screen.onkey(go_up , "w")

game_on = True
while game_on:
    for car in cars:
        car.backward(car_move)
    time.sleep(0.1)
    screen.update()
    new_car()

    for car in cars:
        if car.distance(turtle) < 20:
            game_on = False
            turtle.penup()
            turtle.goto(-10,0)
            turtle.write("Game Over", align="left", font=("Arial", 20, "normal"))






screen.exitonclick()