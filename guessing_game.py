import random
number = random.randint(1,100)

print("GUESS A NUMBER")
attempts = 6

while True:
    if int(attempts) == 0:
        print("Sorry, You are out of attemps!")
        break

    try :
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input! Please enter a number")

    if guess < number:
        print("Guess is too low, "+str(attempts)+" attempts left")
        attempts = int(attempts) - 1
        continue
    elif guess > number:
        print("Guess is too high, "+str(attempts)+" attempts left")
        attempts = int(attempts) - 1
        continue
    else:
        print("Correct, "+str(number)+" was the random number!")
        break
    