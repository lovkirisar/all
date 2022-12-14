import turtle
t = turtle.Turtle()
t.shape()
t.width(5)
t.color('green')
t.penup()
t.speed(0)

t.goto(-390,-270)
t.width(90)
t.pendown()
t.goto(390,-270)
t.penup()

t.color('cyan')
t.width(550)
t.goto(390,50)
t.pendown()
t.goto(-390,50)
t.penup()

t.color('brown')
t.width(1)
t.goto(250,-290)
t.fillcolor('brown')
t.begin_fill()
t.pendown()
t.goto(270,-290)
t.goto(270,100)
t.goto(250,100)
t.goto(250,-290)
t.end_fill()
t.penup()

t.color('green')
t.goto(260, 100)
t.fillcolor('green')
t.begin_fill()
t.pendown()
t.circle(75)
t.end_fill()
t.penup()
t.goto(260,-100)
t.begin_fill()
t.pendown()
t.circle(120)
t.end_fill()
t.penup()

t.color('brown')
t.width(1)
t.goto(-250,-290)
t.fillcolor('brown')
t.begin_fill()
t.pendown()
t.goto(-270,-290)
t.goto(-270,100)
t.goto(-250,100)
t.goto(-250,-290)
t.end_fill()
t.penup()

t.color('green')
t.goto(-260, 100)
t.fillcolor('green')
t.begin_fill()
t.pendown()
t.circle(75)
t.end_fill()
t.penup()
t.goto(-260,-100)
t.begin_fill()
t.pendown()
t.circle(120)
t.end_fill()
t.penup()

t.goto(-100,-280)
t.color('orange')
t.fillcolor('orange')
t.begin_fill()
t.pendown()
for i in range(4):
 t.forward(200)
 t.left(90)
t.end_fill()
t.penup()

t.goto(0,0)
t.color('red')
t.fillcolor('red')
t.begin_fill()
t.pendown()
t.goto(125,-80)
t.goto(-125,-80)
t.end_fill()
t.penup()

t.goto(-50,-230)
t.width(5)
t.color('black')
t.fillcolor('blue')
t.begin_fill()
t.pendown()
for i in range(4):
 t.forward(100)
 t.left(90)
t.end_fill()
t.penup()

t.goto(-50, -180)
t.pendown()
t.goto(50, -180)
t.penup()
t.goto(0, -230)
t.pendown()
t.goto(0, -130)
t.penup()

t.goto(-25, 230)
t.color('yellow')
t.fillcolor('yellow')
t.begin_fill()
t.pendown()
t.circle(50)
t.end_fill()
t.penup()

r = 5

t.goto(-25, 270)
t.right(180)
t.pendown()
for i in range(10):
 t.width(r)
 t.left(18)
 for i in range(10):
  t.forward(20)
  r = r + 1
  t.width(r)
  t.forward(0.05)
 r = 5
 t.backward(200)



turtle.done()