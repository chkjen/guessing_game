import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"OK, guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low!")
        elif guess > random_number:
            print("Sorry, guess again. Too high!")

    print(f"Congrats! You have guessed the number {random_number}\n")
    computer_guess(x)

def computer_guess(x):
    print("Ok, you think of a number within the same limits now and I'll guess.\n")
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        guess = random.randint(low,high)
        feedback = input(f"Is my {guess} too high (H), too low (L) or correct (C)? ").lower()
        if feedback == "h":
            high = guess -1
        elif feedback == "l":
            low = guess + 1

    print (f"Yay, I guessed your number, {guess}, correctly!")




top_value = int(input("Let's play a guess the numbers game. Tell me the maximum number please: "))
guess(top_value)