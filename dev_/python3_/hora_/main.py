# Python Turtle Clock - www.101computing.net/python-turtle-clock/

# Unfortunately the datetime library is not available on this online tool so we cannot retrieve the current time
#from datetime import datetime

import turtle

myPen = turtle.Turtle()
myPen.shape("arrow")
myPen.tracer(0)
myPen.speed(0)

#currentMinute = datetime.datetime.now().minute
#currentHour = datetime.datetime.now().hour
currentMinute=48
currentHour=2

myPen.penup()
myPen.goto(0,-180)
myPen.pendown()
myPen.color("blue")
myPen.circle(180)

myPen.color("red")

myPen.penup()
myPen.goto(0,0)
myPen.setheading(90) # Point to the top - 12 o'clock
myPen.right(currentHour*360/12)
myPen.pendown()
myPen.forward(100)

myPen.penup()
myPen.goto(0,0)
myPen.setheading(90) # Point to the top - 0 minute
myPen.right(currentMinute*360/60)
myPen.pendown()
myPen.forward(150)


myPen.getscreen().update()
