import random
from colorama import Fore
number = random.randint(1,100)


print("GUESS A NUMBER")
attempts = 6

while True:
    if int(attempts) == 0:
        print(Fore.RED +"Sorry, You are out of attemps!" + Fore.RESET)
        break

    try :
        guess = int(input(Fore.CYAN +"Enter your guess: " + Fore.RESET))
    except ValueError:
        print(Fore.RED +"Invalid input! Please enter a number" + Fore.RESET)

    if guess < number:
        print(Fore.RED +"Guess is too low, "+str(attempts)+" attempts left" + Fore.RESET)
        attempts = int(attempts) - 1
        continue
    elif guess > number:
        print(Fore.RED +"Guess is too high, "+str(attempts)+" attempts left" + Fore.RESET)
        attempts = int(attempts) - 1
        continue
    else:
        print(Fore.GREEN +"Correct, "+str(number)+" was the random number!" + Fore.RESET)
        break
    