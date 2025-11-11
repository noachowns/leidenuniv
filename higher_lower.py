import random

print("Welcome to Higher & Lower, a game where you have 5 attempts to guess the correct number.")
print("When you forgot your previous attempts you can guess -1 which does not count as a guess")
print("but will print your previous guesses!")

# Asks the user a range in where he can guess the radom generated number
max_number = int(input("Choose the guessing range starting from 1 to: "))
# Generates a random number that will has to be guessed
secret_number = random.randint(1, max_number)

# Variables that track the amount of guesses, attempts and points/system
guesses = []
attempts = 0
points = 0
max_attempts = 5
points_table = [10, 8, 5, 2, 1]

# Main game while loop, runs 5 times
while attempts < max_attempts:
    guess = int(input(f"Guess a number between 1 and {max_number}: "))

    # Check if player entered -1 to see their previous guesses:
    if guess == -1:
        if len(guesses) == 0:
            print("You haven't made any guesses yet")  # If there have not been made any guesses
        else:
            print("You have tried to following numbers: ", end=" ")
            for number in guesses:
                print(number, end=" ")
        print()
        continue  # Continues and goes back to beginning. -1 will not be a guess now

    # Keeps track of guess and increase attempts count. Adds to list and counts it
    guesses.append(guess)
    attempts += 1

    # If the guess is correct:
    if guess == secret_number:

        points = points_table[attempts - 1]  # Awards points based on which attempt it was (10,8,5,2,1)
        print("You have tried to following numbers:", end=" ")
        for number in guesses:
            print(number, end=" ")
        print()
        print(f"to guess the secret number {secret_number}!")
        print(f"You won and are awarded {points} points!")
        break  # Exits loop because it is CORRECT

    # Gives hint when the guess is lower or higher than the secret number
    elif guess < secret_number:
        print(f"{guess} is incorrect, the number is higher.")
        print()
    else:
        print(f"{guess} is incorrect, the number is lower.")
        print()

# When the player looses it prints the previous guesses and the secret number they were supposed to guess
if points == 0:
    print("You have tried to following numbers:", end=" ")
    for number in guesses:
        print(number, end=" ")
    print(f" to guess the secret number {secret_number}!")
    print("You lost :(")
