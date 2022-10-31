import turtle, random, time
t = turtle.Turtle()
t. shape()
t.width(5)
t.color('red')
t.speed(0)
t.penup()

t.goto(125,0)

сolors = ['green','blue','yellow']

t.pendown()

for i in range(4):
    for i in range(12):
        t.circle(50, 30, 25)
        t.color(random.choice(colors))
        t.circle(50, 360, 4)
    t.color('red')
    t.right(180)
    t.circle(100,90,25)    
     
     
 
turtle.done() 