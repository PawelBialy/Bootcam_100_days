from turtle import Turtle, Screen, shapesize

tim = Turtle()

tim.shape("classic")
tim.color("red")

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
####Right Version 
colors = ["cyan", "light sea green","khaki","slate blue", "black", "light green","teal",
          "pale violet red","spring green" ]
def draw_shape(num_of_side):
    angle = 360 / num_of_side
    for _ in range(num_of_side):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3,11):
    draw_shape(shape_side_n)
    tim.color(random.choice(colors))

#######First Version
# for _ in range(3):
#     tim.forward(100)
#     tim.right(120)
#     tim.color("blue")
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
#     tim.color("red")
# for _ in range(5):
#     tim.forward(100)
#     tim.right(72)
#     tim.color("gray")
# for _ in range(6):
#     tim.forward(100)
#     tim.right(60)
#     tim.color("black")
# for _ in range(7):
#     tim.forward(100)
#     tim.right(51.42)
#     tim.color("brown")
# for _ in range (8):
#     tim.forward(100)
#     tim.right(45)
#     tim.color("gold")
# for _ in range (9):
#     tim.forward(100)
#     tim.right(40)
#     tim.color("pink")
# for _ in range (10):
#     tim.forward(100)
#     tim.right(36)
#     tim.color("gold2")
# tim.color("blue")
# tim.forward(100)















screen = Screen()
screen.exitonclick()
