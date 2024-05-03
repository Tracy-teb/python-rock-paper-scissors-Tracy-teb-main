#import random choice from python library
from random import choice

#define the choices
choices = ["rock", "paper", "scissors"]

#defining a function and rules of the game
def game_winner (computer_choice, human_choice):
    if computer_choice == human_choice:
        return 'A tie'
    elif ((computer_choice == 'rock' and human_choice == 'scissors') or
          (computer_choice == 'paper' and human_choice == 'rock') or
          (computer_choice == 'scissors' and human_choice == 'paper')):
        return computer_choice
    else:
        return human_choice
    
#Function to play the game 
def play_game(max_rounds):
    human_score = 0
    computer_score = 0
    round_count = 0

    while round_count < max_rounds:
        round_count += 1
        computer_choice = choice(choices)
        human_choice = input(f"round{round_count}: 'rock','paper', or 'scissors': ")

        if human_choice not in choices:
            print("Invalid choice. Try Again.")
            continue

        result = game_winner(computer_choice, human_choice)

        if result == "computer":
            computer_score += 1
            print(f"You chose{human_choice}, and the computer chose{computer_choice}. The computer wins this round!")
        elif result == "human":
            human_score += 1
            print(f"You chose{human_choice}, and the computer chose{computer_choice}. You win this round!")
        else:
            print(f"You both chose {human_choice}. It is a tie!")

        print(f"score: You {human_score} - computer {computer_score}")

        if human_score == max_rounds // 2 + 1 or computer_score == max_rounds // 2 + 1:
            break

        if human_score > computer_score:
            print("Congratulations ! You win the game!")
        elif human_score < computer_score:
            print("Sorry, the computer wins the game.")
        else:
            print("It is a tie game!")

play_game(5)



