import turtle
bob = turtle.Turtle()

'''
Task 1: Create a flower function that accepts a coordinate
and draws a flower at that location.  Use comet() design
developed in Lesson 16 Discussion and simply add a stem.
'''

def flower1(x,y,size,c1,c2):
  bob.color("brown")
  bob.pensize(5)
  bob.right(90)
  bob.forward(30)
  jump(x,y)
  bob.setheading(0) # sets turtle orientation angle
  for times in range(12):
    jump(x,y)
    bob.setheading(0)
    bob.left(times * 30 )
    comet(c1,size,8)
  for times in range(12):
    jump(x,y)
    bob.setheading(0)
    bob.left(times * 30 + 15)
    comet(c2,size,8)


def flower2(x,y,c,size):
  jump(x,y)
  bob.color(c)
  for times in range(10):
    bob.left(36)
    bob.circle(size)

# stick (stem for flower)
def stick( c ):
  bob.color( c )
  bob.circle(20)
  bob.right(90)
  bob.forward(50)
  jump(-20,-20)
  bob.left(90)
  bob.forward(40)
  
def sun(x,y):
  jump(x,y)
  bob.pensize(10)
  bob.color("yellow")
  for times in range(10):
    polygon(3,20)
    bob.forward(30)
    bob.right(36)
  jump(16 + x,-75 + y)
  bob.pensize(20)
  bob.circle(30)
  
def tree1(x,y):
  jump(x,y)
  bob.pensize(5)
  bob.color("brown")
  polygon(4, 50)
  jump(-25 + x , 50 + y)
  bob.color("green")
  polygon(3, 100)
  jump(-25 + x, 75 + y)
  polygon(3, 100)

def tree2(x,y):
  jump(x,y)
  bob.pensize(5)
  bob.color("brown")
  polygon(4, 50)
  bob.color("green")
  jump(-10 + x, 50 + y)
  bob.circle(40)
  jump(60 + x, 50 + y)
  bob.circle(40)
  jump(25 + x, 75 + y)
  bob.circle(40)
  jump(25 + x, 25 + y)
  bob.circle(40)

def polygon(sides, distance ):
  angle = 360 / sides
  for times in range(sides):
    bob.forward(distance)
    bob.left(angle)

def comet(c, distance, angle):
  bob.color(c)
  for times in range(10):
    bob.pensize(times / 2)
    bob.forward(distance)
    bob.left(angle)

def jump(x,y):
  bob.penup()
  bob.goto(x,y)
  bob.pendown()

def home():
  bob.penup()
  bob.home()
  #moves turtle to origin (0,0) & resets start orientation
  bob.pendown()

def rainbow():
  bob.width(20)
  bob.color("red")
  bob.circle(60)
  bob.color("orange")
  bob.circle(50)
  bob.color("yellow")
  bob.circle(40)
  bob.color("green")
  bob.circle(30)
  bob.color("blue")
  bob.circle(20)
  bob.color("purple")
  bob.circle(10)

def plus(c,distance):
  bob.color(c)
  for times in range(4):
    bob.forward(distance)
    bob.left(90)
    bob.forward(distance)
    bob.right(90)
    bob.forward(distance)
    bob.left(90)
