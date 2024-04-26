import random

number = random.randint(1,10)

total_guess = 0

while total_guess < 3:
    guess = int(input('Enter your guess,human : '))
    if guess > number:
        print('Your Guess is a bit high,guess a bit low')
        total_guess += 1
    elif guess < number:
        print('Your Guess is a bit low,guess a bit high')
        total_guess += 1
    else:
        print('Your Guess is right')
        break

print(' \nGAME OVER  ')