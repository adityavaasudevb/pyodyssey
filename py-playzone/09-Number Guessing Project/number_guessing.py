import random
num = random.randint(1, 100)

from art import logo
print(logo)

def function(turns):
    while turns >= 0:
        if turns==0:
            print("You've run out of guesses, you lose.")
            break
        print(f"You have {turns} attempts remaining to guess the number")
        turns -= 1
        guess=int(input("Make a guess: "))
        if guess==num:
            print(f"You got it! The answer was {num}.")
            break
        elif guess>num:
            print("Too high.\nGuess again.")
        else:
            print("Too low.\nGuess again.")

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty=="easy":
    function(10)
else:
    function(5)


