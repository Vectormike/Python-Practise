
try:
    number  = int(input("Enter a number: \n"))
except ValueError:
    print('Enter a valid number')

def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    elif number % 2 != 0:
        result = (3 * number + 1)
        print(result)
        return result
collatz(number)