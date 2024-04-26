import random

print('----------- Lets Begin -------------')
print(' ----Can you guess the number? -----')
print('Remember you only have 3 attempts')


my_number = int(input("Enter the number to guess : "))

attempt = 0
low = int(input('Enter your lowest point in the range : '))
high = int(input('Enter your highest point in the range : '))

while attempt < 3:
    guess1 = random.randint(low, high)
    if guess1 > my_number:
        print(f"{guess1} is High.\nHint: Guess Low")
        attempt += 1

        guess2 = random.randint(low,guess1)
        if guess2 > my_number:
            print(f"{guess2} is High.\nHint: Guess Low")
            attempt += 1

            guess3 = random.randint(low,guess2)
            if guess3 > my_number:
                print(f'{guess3} is wrong.\n Unfortunately No Guesses Left')
                attempt += 1

            elif guess3 < my_number:
                print(f'{guess3} is wrong.\n Unfortunately No Guesses Left')
                attempt += 1

        elif guess2 < my_number:
            print(f"{guess2} is Low.\nHint: Guess High")
            attempt += 1

            guess3 = random.randint(guess2,guess1)

            if guess3 > my_number:
                print(f'{guess3} is wrong.\n Unfortunately No Guesses Left')
                attempt += 1

            elif guess3 < my_number:
                print(f'{guess3} is wrong.\n Unfortunately No Guesses Left')
                attempt += 1

    elif guess1 < my_number:
        print(f"{guess1} is Low.\nHint: Guess High")
        attempt += 1

        guess2 = random.randint(guess1,high)

        if guess2 > my_number:
            print(f"{guess2} is High.\nHint: Guess Low")
            attempt += 1

            guess3 = random.randint(guess1,guess2)
            if guess3 > my_number:
                print(f'{guess3} is wrong.\n Unfortunately No Guesses Left')
                attempt += 1

            elif guess3 < my_number:
                print(f'{guess3} is wrong.\n Unfortunately No Guesses Left')
                attempt += 1

        elif guess2 < my_number:
            print(f"{guess2} is Low.\nHint: Guess High")
            attempt += 1

            guess3 = random.randint(guess2,high)

            if guess3 > my_number:
                print(f'{guess3} is wrong.\n Unfortunately No Guesses Left')
                attempt += 1

            elif guess3 < my_number:
                print(f'{guess3} is wrong.\n Unfortunately No Guesses Left')
                attempt += 1

    else:
        print('Guess is Right')
        break