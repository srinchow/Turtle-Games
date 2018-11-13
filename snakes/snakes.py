import turtle 
import random
import os
import time
import tkinter

##screen 
sc=turtle.Screen()
sc.title("Snake game")
sc.bgcolor("black")
sc.setup(width=800,height=800)
sc.tracer(0)


### bait object
bait=turtle.Turtle()
bait.shape('circle')
bait.shapesize(1,1)
bait.color('red')
bait.penup()
bait.goto(0,100)

###snake object
snake=turtle.Turtle()
snake.color('white')
snake.shape('square')
snake.shapesize(0.9,0.9)
snake.penup()
snake.goto(2,2)
snake.speed(0)
snake.direction="stop"

###Functions to move 
def go_up():
    if snake.direction!="down":
        snake.direction="up"

def go_left():
    if snake.direction!="right":
        snake.direction="left"


def go_down():
    if snake.direction!="up":
        snake.direction="down"

def go_right():
    if snake.direction!="left":
        snake.direction="right"

## movements

def movement():
    if snake.direction=="left":
        snake.setx(snake.xcor()-0.025)

    if snake.direction=="right":
        snake.setx(snake.xcor()+0.025)
    
    if snake.direction=="down":
        snake.sety(snake.ycor()-0.025)
    
    if snake.direction=="up":
        snake.sety(snake.ycor()+0.025)

sc.listen()
sc.onkeypress(go_up,"w")
sc.onkeypress(go_down,"s")
sc.onkeypress(go_left,"a")
sc.onkeypress(go_right,"d")








### game loop
while True:
    sc.update()

    if snake.xcor()<-394:
        snake.setx(394)
    if snake.xcor()>394:
        snake.setx(-394)
    if snake.ycor()<-394:
        snake.sety(394)
    if snake.ycor()<-394:
        snake.sety(394)
    

    movement()


