import random
number = random.randint(1, 100)
while True: 
    guess = input('guess the number: ')
    guess = int(guess)
    if guess == number:
        print('you are right')
        break 
    elif guess > number:
        print('too big')
    elif guess < number:
        print('to small')