from random import *
from turtle import *
speed(15)

penup()
goto(-140,140)
for step in range(15):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)
    
bob = Turtle()
bob.color('deep sky blue')
bob.shape('turtle')
bob.penup()
bob.goto(-160,100)
pendown()

sally = Turtle()
sally.color('blue')
sally.shape('turtle')
sally.penup()
sally.goto(-160,70)
pendown()

mary = Turtle()
mary.color('deep pink')
mary.shape('turtle')
mary.penup()
mary.goto(-160,40)
pendown()

peter = Turtle()
peter.color('green')
peter.shape('turtle')
peter.penup()
peter.goto(-160,10)
pendown()

turns = 0
while turns < 100:
    bob.forward(randint(1,5))
    sally.forward(randint(1,5))
    mary.forward(randint(1,5))
    peter.forward(randint(1,5))
    turns += 1

for twirl in range(10):    
    bob.left(36)
    sally.left(36)
    mary.right(36)
    peter.right(36)
