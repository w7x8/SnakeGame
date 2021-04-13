# Snake game made by GitHub user w7x8

import turtle
import time
import random


delay = 0.095


score = 0
hscore = 0


turt = turtle.Screen()
turt.title("Snake")
turt.bgcolor("snow")
turt.setup(width=800, height=800)
turt.tracer(0)


head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"


apple = turtle.Turtle()
apple.speed(0)
apple.shape("circle")
apple.color("red")
apple.penup()
apple.goto(0,100)

body = []


pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 360)
pen.write("Score: 0  High Score: 0", align="center", font=("Helvetica", 26, "normal"))


def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


turt.listen()
turt.onkeypress(go_up, "w")
turt.onkeypress(go_down, "s")
turt.onkeypress(go_left, "a")
turt.onkeypress(go_right, "d")

turt.onkeypress(go_up, "W")
turt.onkeypress(go_down, "S")
turt.onkeypress(go_left, "A")
turt.onkeypress(go_right, "D")

turt.onkeypress(go_up, "Up")
turt.onkeypress(go_down, "Down")
turt.onkeypress(go_left, "Left")
turt.onkeypress(go_right, "Right")


while True:
    turt.update()

    
    if head.xcor()>360 or head.xcor()<-360 or head.ycor()>360 or head.ycor()<-360:
        time.sleep(1.5)
        head.goto(0,0)
        head.direction = "stop"

           
        for part in body:
            part.goto(1000, 1000)
        
        
        body.clear()

        
        score = 0

        
        delay = 0.095

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, hscore), align="center", font=("Helvetica", 26, "normal")) 


    
    if head.distance(apple) < 20:
        
        x = random.randint(-360, 360)
        y = random.randint(-360, 360)
        apple.goto(x,y)

        
        new_part = turtle.Turtle()
        new_part.speed(0)
        new_part.shape("square")
        new_part.color("black")
        new_part.penup()
        body.append(new_part)

        
        delay -= 0.001

        
        score += 1

        if score > hscore:
            hscore = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, hscore), align="center", font=("Helvetica", 26, "normal")) 

    
    for index in range(len(body)-1, 0, -1):
        x = body[index-1].xcor()
        y = body[index-1].ycor()
        body[index].goto(x, y)

    
    if len(body) > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x,y)

    move()    

    
    for part in body:
        if part.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            
            for part in body:
                part.goto(1000, 1000)
        
            
            body.clear()

            
            score = 0

            
            delay = 0.095
        
            
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, hscore), align="center", font=("Helvetica", 26, "normal"))

    time.sleep(delay)

turt.mainloop()
