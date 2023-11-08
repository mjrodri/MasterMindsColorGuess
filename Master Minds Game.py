#Objectives
#Generate a 4 color random code
#Make the user guess the code
#Compare each guess to real code. Determine number of correct and incorrect inputs. 
#Tie the game together. Determine if user inputs are correct or if they lost the game. 

import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

#funtion that generates the code

def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.apend(color)

    return code

#Function to Allow user to guess the code

def guess_code():
    while True:
        guess = input("Guess: ").upper().split(" ")

        if len(guess) is CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try Again.")
                break
        else:
            break

    return guess

#Check inputs to see how many ae correct. Comparing the correct code to the user entered. 

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

        return correct_pos, incorrect_pos
    
def game():
    print(f"Welcome to Master Mind! You have {TRIES} to guess the code...")
    print("The valide colors are", *COLORS)

    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")
            break

        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")

    else:
        print("You ran out of tries, the code was:", *code)


if __name__ == "__main__":
    game()
