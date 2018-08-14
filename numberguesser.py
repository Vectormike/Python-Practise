# This is a guess number game
import random

secretNumber = int(input("Enter a number between 1 to 10: /n"))

secretNumber = random.randint(1, 10)

for i in secretNumber:
    if