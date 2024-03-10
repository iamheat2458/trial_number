import random
number = random.randint(1, 100)
count = 0
while True: 
    count = count + 1 
    guess = input('guess the number: ')
    guess = int(guess)
    if guess == number:
        print('you are right')
        print('it is your', count, 'times')
        break 
    elif guess > number:
        print('too big')
    elif guess < number:
        print('to small')
    print('it is your', count, 'times')