#import random choice from python library
from random import choice

#defining a function and rules of the game
def game_winner (computer_choice, human_choice):
    if computer_choice == human_choice:
        return 'A tie'
    elif ((computer_choice == 'rock' and human_choice == 'scissors') or
          (computer_choice == 'paper' and human_choice == 'rock') or
          (computer_choice == 'scissors' and human_choice == 'paper')):
        return f'computer chose {computer_choice}. computer wins!'
    else:
        return f'computer chose{computer_choice}. human wins!'
    
#Get ccomputer choice 
computer_choice = choice(['rock', 'paper', 'scissors'])

#Get human choice 
human_choice = input("enter 'rock', 'paper', or 'scissors':")

#Call the result
result = game_winner(computer_choice, human_choice)

print(result)


