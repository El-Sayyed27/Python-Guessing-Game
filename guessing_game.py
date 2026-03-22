import random
from playsound import playsound
from colorama import Fore
number = random.randint(1,100)


print("GUESS A NUMBER")
attempts = 6

while True:
    if int(attempts) == 0:
        print(Fore.RED +"Sorry, You are out of attemps!")
        break

    try :
        guess = int(input(Fore.CYAN +"Enter your guess: "))
    except ValueError:
        print(Fore.RED +"Invalid input! Please enter a number")

    if guess < number:
        playsound(r"sounds/wrong-answer.wav")
        print(Fore.RED +"Guess is too low, "+str(attempts)+" attempts left")
        attempts = int(attempts) - 1
        continue
    elif guess > number:
        playsound(r"sounds/wrong-answer.wav")
        print(Fore.RED +"Guess is too high, "+str(attempts)+" attempts left")
        attempts = int(attempts) - 1
        continue
    else:
        playsound(r"sounds/correct-answer.wav")
        print(Fore.GREEN +"Correct, "+str(number)+" was the random number!")
        break
    