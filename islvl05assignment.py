#Jenna Smedley
#Rock paper scissors game (lvl 05 assignment)

import random
num_rounds = 0
program_plays = ['rock', 'paper', 'scissors']
program_wins = 0
user_wins = 0
round_counter = 0

#function to determine who the winner is
def determine_winner(y):
    program_play = random.choice(program_plays)
    print(f"The program chose {program_play}.")
    if y.lower() == program_play:
        return "tie"
    elif y.lower() == "rock":
        if program_play == "scissors":
            return "user"
        elif program_play == "paper":
            return "program"
    elif y.lower() == "paper":
        if program_play == "rock":
            return "user"
        elif program_play == "scissors":
            return "program"
    elif y.lower() == "scissors":
        if program_play == "paper":
            return "user"
        elif program_play == "rock":
            return "program"

#function to ask the user for their choice
def get_player_choice():
    while True:
        x = input("Rock, Paper, or Scissors? ")
        if x.lower() in ("rock", "paper", "scissors"):
            return x
        print("Invalid input. Try again.")
        
#welcome user to game
print("Welcome user. Let the battle of Rock, Paper, Scissors commence.")

#ask user for number of rounds
while num_rounds % 2 == 0 or num_rounds <= 0:
    num_rounds = int(input("Enter how many rounds you'd like to play: "))
    if num_rounds % 2 == 0:
        print("Invalid input. Please enter a positive odd number.")

#main gameplay function
while round_counter < num_rounds:
    user_play = get_player_choice()
    who_won = determine_winner(user_play)
    if who_won == "tie":
        print("Tie! Try again.")
    elif who_won == "user":
        print("You win!")
        user_wins += 1
        round_counter += 1
    elif who_won == "program":
        print("You lose!")
        program_wins += 1
        round_counter += 1

#game ending sequence
print("The game is finished.")
print(f"You won {user_wins} times.")
print(f"I won {program_wins} times.")
if user_wins > program_wins:
    print("The ultimate winner is the user. Well done.")
elif user_wins < program_wins:
    print("The ultimate winner is the program. I must go away to revel in my glory. Goodbye")


