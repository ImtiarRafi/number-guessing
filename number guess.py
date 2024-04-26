import random

my_number = int(input("Enter the number : "))

attempt = 0

while attempt < 3:
    guess1 = random.randint(1, 10)
    if guess1 > my_number:
        print('Guess', {guess1}, ' is High')
        attempt += 1

        guess2 = random.randint(1,guess1)
        if guess2 > my_number:
            print('Guess', {guess2}, ' is High')
            attempt += 1

            guess3 = random.randint(1,guess2)
            if guess3 > my_number:
                print('No Guess Left')
                attempt += 1

            elif guess3 < my_number:
                print('No Guess Left')
                attempt += 1

        elif guess2 < my_number:
            print('Guess', {guess2}, ' is low')
            attempt += 1

            guess3 = random.randint(guess2,guess1)

            if guess3 > my_number:
                print('No Guess Left')
                attempt += 1

            elif guess3 < my_number:
                print('No Guess Left')
                attempt += 1
    elif guess1 < my_number:
        print('Guess',{guess1},'is low')
        attempt += 1

        guess2 = random.randint(guess1,10)

        if guess2 > my_number:
            print('Guess', {guess2}, ' is High')
            attempt += 1

            guess3 = random.randint(guess1,guess2)
            if guess3 > my_number:
                print('No Guess Left')
                attempt += 1

            elif guess3 < my_number:
                print('No Guess Left')
                attempt += 1

        elif guess2 < my_number:
            print('Guess', {guess2}, ' is low')
            attempt += 1

            guess3 = random.randint(guess2,10)

            if guess3 > my_number:
                print('No Guess Left')
                attempt += 1

            elif guess3 < my_number:
                print('No Guess Left')
                attempt += 1

    else:
        print('Guess is Right')