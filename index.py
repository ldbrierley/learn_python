import random

def get_guess():
    while True:
        try:
            guess = input("What is your guess: ")
            int(guess)
            return guess
        except:
            print("That did not work please type an number")

the_random_number = random.randint(1,20)

print("Welcome to the number guessing game.")
print("Guess a number between 1 and 20 and I will tell you if it was to small or too big")
number_of_guesses = 0
while True:
    guess = get_guess()
    number_of_guesses += 1
    print("You have done " + str(number_of_guesses) + " Attempts")
    if guess == the_random_number:
        print("correct")
        break
    elif guess > the_random_number:
        print("You guess to high")
    else:
        print("You guess to low")

score = 100 / number_of_guesses
print("score is " + str(score)) 