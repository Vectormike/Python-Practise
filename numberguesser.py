# This is a guess number game
import random

secretNumber = random.randint(1, 21)
print("I have a number within a range of 1 to 20")

4
# Ask the user to guess 10x
for guessTaken in range(1, 30):
    guess = int(input("Guess: "))
    if guess < secretNumber:
        print("Your number is low")
    elif guess > secretNumber:
        print("Your guess is high")
    elif guess == secretNumber:
        print("Wow! It's actually " + str(secretNumber) + " and you guessed " + str(guessTaken) + ' times.')
    else:
        print("You're wrong.")