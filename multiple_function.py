print("Thhs is gonna be multiple function. I'll be passing in arguments to the function I created 'octagon()'.. watch out!")

import turtle

maryann = turtle.Turtle()

def octagon(lenght, angle):

    maryann.forward(lenght)
    maryann.left(angle)
    maryann.forward(lenght)
    maryann.left(angle)
    maryann.forward(lenght)
    maryann.left(angle)
    maryann.forward(lenght)
    maryann.left(angle)
    maryann.forward(lenght)
    maryann.left(angle)
    maryann.forward(lenght)
    maryann.left(angle)
    maryann.forward(lenght)
    maryann.left(angle)
    maryann.forward(lenght)
    maryann.left(angle)
    maryann.forward(50)
    maryann.right(90)
    maryann.forward(60)
    
octagon(100, 45)
maryann.forward(60)

octagon(100, 45)
maryann.forward(60)
octagon(100, 45)
maryann.forward(60)
octagon(100, 45)
maryann.forward(110)

print("That was cool!")
