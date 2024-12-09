import random

low = 1
up = 100
num_guess = 0

def conditional(a, b):
    if b > a:
            print("high")
    elif b < a:
            print("low")
    else:
            print("error")


def higher_lower():
    num_list = [60, 18, 32, 86, 70, 15, 29, 39, 67, 75, 28, 11, 48, 80, 84, 35, 24, 68]
    num = random.choice(num_list)
    guess = int(input("What is your guess? "))
    num_guess = 0

    while num != guess:
        conditional(num, guess)
    
        num_guess += 1
        guess = int(input("What is your guess? "))
    print("Good Job, you've guessed the number in " + str(num_guess))


higher_lower()


