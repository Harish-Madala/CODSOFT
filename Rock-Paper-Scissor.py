import random

def display_choices(user_choice, computer_choice):
    print(f"\nYou chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_result(winner):
    if winner == "user":
        print("You win this round!")
    elif winner == "computer":
        print("Computer wins this round.")
    else:
        print("It's a tie!")

def main():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    print("=== Rock-Paper-Scissors Game ===")

    while True:
        user_choice = input("\nEnter your choice (rock, paper, scissors): ").lower()

        if user_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        display_choices(user_choice, computer_choice)

        winner = determine_winner(user_choice, computer_choice)
        display_result(winner)

        # Update scores
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"\nScores - You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing! Final Scores:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break

if __name__ == "__main__":
    main()
