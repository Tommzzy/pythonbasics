
import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (
        (player == "r" and computer == "s") or
        (player == "s" and computer == "p") or
        (player == "p" and computer == "r")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print(" Welcome to Rock, Paper, Scissors!")
    while True:
        player_choice = input("\nChoose r for rock, p for paper, or s for scissors (or 'quit' to stop): ").lower()

        if player_choice == "quit":
            print("Thanks for playing! Goodbye. ")
            break

        if player_choice not in ["r", "p", "s"]:
            print("❌ Invalid choice. Try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

# Start the game :

play_game()
