# Circle Project

import turtle

victor = turtle.Turtle()
victor.speed(0)
def square(length, angle):
    for i in range(4):
        victor.forward(length)
        victor.right(angle)
    
square(100, 90)

victor.right(11)
for i in range(100):
    square(100, 90)
    victor.right(11)
