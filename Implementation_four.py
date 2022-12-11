
import random

# Define the choices that the player can make
choices = ["rock", "paper", "scissors", "lizard", "spock"]

# Define the rules of the game
rules = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["paper", "spock"],
    "spock": ["rock", "scissors"]
}

# Start the game
print("Welcome to Rock Paper Scissors Lizard Spock!")

# Get the player's choice
player_choice = input("Choose one: rock, paper, scissors, lizard, or spock: ").lower()

# Check if the player's choice is valid
if player_choice not in choices:
    print("Invalid choice. Please try again.")
    exit()

# Choose a random choice for the computer
computer_choice = random.choice(choices)

# Check who wins
if player_choice == computer_choice:
    print("It's a tie!")
elif computer_choice in rules[player_choice]:
    print("You win! {} beats {}".format(player_choice, computer_choice))
else:
    print("You lose! {} beats {}".format(computer_choice, player_choice))
