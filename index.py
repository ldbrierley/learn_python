import random

def get_guess():
    while True:
        try:
            guess = input("What is your guess: ")
            int(guess)
            return guess
        except:
            print("That did not work please type an number")

the_random_number = random.randint(1,500)

print("Welcome to the number guessing game.")
print("Guess a number between 1 and 500 and I will tell you if it was to small or two big")

while True:
    guess = get_guess()
    if guess == the_random_number:
        print("correct")
        break
     
    elif guess > the_random_number:
        print("You guess to high")
     
    else:
        print("You guess to low")
    

