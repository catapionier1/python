import turtle
s=turtle.Screen()
s.bgcolor('green')






p=turtle.Turtle()
p.pensize(10)
p.color('blue')
p.shape('triangle')
p.speed(0)
p.penup()
p.setposition(0,-270)
pspeed=30


b=turtle.Turtle()
b.penup()
b.setposition(-300,-300)
b.pendown()
b.pensize(3)
for side in range (4):
    b.forward(600)
    b.left(90)
b.hideturtle()



speed=1


def move_left(x,y):
    z=p.xcor()
    
    z-=pspeed
    p.setx(z)


def move_right(y,x):
    
    z=p.xcor()
    z+=pspeed
    p.setx(z)

    



turtle.listen()
turtle.onscreenclick(move_left, 1)



turtle.listen()
turtle.onscreenclick(move_right, 3)

        







 









turtle.done()
