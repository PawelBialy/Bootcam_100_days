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

        ### Random walk ###  
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))
 

 ####Set random color ####

t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color
 
          
          
 ####Spirograph 

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap )):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
draw_spirograph(15)



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
