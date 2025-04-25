import random
import sys

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
YES = 'y'
NO = 'n'

emojis = {ROCK: '🪨', SCISSORS: '✂️', PAPER: '📃'}
choices = tuple(emojis.keys())


def get_user_choice():
    while True:
        user_choice = input("Rock, Paper, or Scissors? (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice")


def display_choices(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Draw :|")
    elif (
            (user_choice == ROCK and computer_choice == SCISSORS) or
            (user_choice == SCISSORS and computer_choice == PAPER) or
            (user_choice == PAPER and computer_choice == ROCK)):
        print("You win :)")
    else:
        print("You lose :(")


def main():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        while True:
            keep_playing = input("\nDo you want to continue? (y/n): ").lower()
            if keep_playing == NO:
                print("Thank you for playing!")
                sys.exit()
            elif keep_playing == YES:
                break
            else:
                print("Invalid choice")


main()
