import random

# Score variables
user_score = 0
computer_score = 0

print("Welcome to Rock-Paper-Scissors Game!")
print("Choose: rock, paper, or scissors")

while True:
    # User input
    user_choice = input("\nEnter your choice: ").lower()

    # Check valid input
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    # Computer random choice
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    # Display choices
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    # Game logic
    if user_choice == computer_choice:
        print("It's a tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
        user_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

    # Display scores
    print("\nScore Board")
    print("Your Score:", user_score)
    print("Computer Score:", computer_score)

    # Play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThanks for playing!")
        break