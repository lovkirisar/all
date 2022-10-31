import turtle
t = turtle.Turtle()
t.shape()
t.width(5)
t.color('green')
t.pendown()

c = 0



for i in range (8):
    t.left(45)
    c = c+1
    if (c==1):
     t.color('green')   
    if (c==2):
     t.color('grey')
    if (c==3):
     t.color('magenta')   
    if (c==4):
     t.color('orange') 
    if (c==5):
      t.color('pink')   
    if (c==6):
      t.color('blue')
    if (c==7):
      t.color('yellow')   
    if (c==8):
      t.color('black')             
    t.circle(100)

        
        
        
turtle.done()