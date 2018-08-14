import turtle

victor = turtle.Turtle()

def square():

    victor.forward(100)
    victor.right(90)
    victor.forward(100)
    victor.right(90)
    victor.forward(100)
    victor.right(90)
    victor.forward(100)
    victor.right(11)

square()

def circle(length, angle):
  
    victor.right(angle)
    victor.forward(length)
    victor.right(angle)
    victor.forward(length)
    victor.right(angle)
    victor.forward(length)
    victor.right(angle)
    victor.forward(length)
    victor.right(angle)
    victor.forward(length)
    victor.right(11)
    
for i in range(100):
    circle(100, 90)

for i in range(100):
    square()
