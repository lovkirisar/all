import turtle
t = turtle.Turtle()
t.shape()
t.width(5)
t.color('red')
t.penup()
t.speed(0)

def krug(x, y, col, r):
    t.color(col)
    t.fillcolor(col)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.penup()
    
krug(-200, -100, 'green', 35)    
krug(-100, -100, 'green', 35)
krug(0, -100, 'green', 35)    
krug(100, -100, 'green', 35)
krug(200, -100, 'green', 35)

t.goto(-200, -100)
t.pendown()
t.color('black')
t.left(180)
t.circle(-36, 180, 25)
t.forward(400)
t.circle(-36, 180, 25)
t.forward(400)
t.penup()

t.goto(-250, -65)
t.right(90)
t.pendown()
t.color('green')
t.width(10)
t.circle(-46, 90, 25)
t.forward(410)
t.circle(-46, 90, 25)
t.penup()

t.color('green')
t.fillcolor('green')
t.goto(-150, -20)
t.pendown()
t.begin_fill()
t.right(225)
t.forward(100)
t.right(45)
t.forward(100)
t.right(45)
t.forward(100)
t.end_fill()
t.penup()

t.width(17)
t.goto(-75, 20)
t.pendown()
t.goto(250, 20)



turtle.done()
    