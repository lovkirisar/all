import turtle
t = turtle.Turtle()
t. shape()
t.width(4)
t.color('red')
t.speed(0)

a = 1

t.penup()
t.goto(100,300)
t.pendown()

for i in range(8):
 while True:
    a = a + 1
    t.circle(-50)
    t.circle(-100, 30, 25)
    t.circle(-50, 360, 4)
    if (a > 12):
          break
 t.penup()        
 a = 1
 t.right(45)
 t.forward(271)
 t.pendown()


turtle.done()