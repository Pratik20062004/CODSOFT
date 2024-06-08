import random

# Choices for the game
choices = ["rock", "paper", "scissors"]

def get_user_choice():
  """Prompts user for their choice and validates input."""
  while True:
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice in choices:
      return user_choice
    else:
      print("Invalid input. Please choose rock, paper, or scissors.")

def get_computer_choice():
  """Generates a random choice for the computer."""
  return random.choice(choices)

def determine_winner(user_choice, computer_choice):
  """Compares user and computer choices and returns the winner."""
  if user_choice == computer_choice:
    return "Tie"
  elif user_choice == "rock":
    if computer_choice == "scissors":
      return "User"
    else:
      return "Computer"
  elif user_choice == "paper":
    if computer_choice == "rock":
      return "User"
    else:
      return "Computer"
  else:  # user_choice == "scissors"
    if computer_choice == "paper":
      return "User"
    else:
      return "Computer"

def play_game():
  """Runs a single round of the game."""
  user_choice = get_user_choice()
  computer_choice = get_computer_choice()
  winner = determine_winner(user_choice, computer_choice)

  print(f"You chose: {user_choice}")
  print(f"Computer chose: {computer_choice}")

  if winner == "Tie":
    print("It's a tie!")
  else:
    print(f"{winner} wins!")

def main():
  """Main function that runs the game loop."""
  print("Welcome to Rock-Paper-Scissors!")
  play_again = "yes"
  while play_again.lower() == "yes":
    play_game()
    play_again = input("Play again? (yes/no): ")

if __name__ == "__main__":
  main()
