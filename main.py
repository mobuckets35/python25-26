#colorfull spiral
import turtle
colors=["red","purple","blue","green","yellow","orange"]
turtle.bgcolor("black")
'''
for x in range(360):
    turtle.pencolor(colors[6])
    turtle.width(x/100+1)
    turtle.forward(x)
    turtle.left(59)
    turtle.speed(200)
    '''
from turtle import*
speed(0)
bgcolor("black")
colors = ['orange', 'white']
hideturtle()
for i in range(122):
    goto(0, 0)
    color(colors[i% 2])
    forward(130)
    left(3)
    circle(40)
    forward(130)
    right(180)



            


