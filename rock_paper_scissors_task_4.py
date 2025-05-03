import random
user_score = 0
computer_score = 0
choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid and try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"You : {user_choice}")
    print(f"Computer : {computer_choice}")
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
        print("Computer win!")
        computer_score += 1

    print(f"Score -> You: {user_score} | Computer: {computer_score}")

    # Ask to play again
    play_again = input("Play again? (yes/nope): ").lower()
    if play_again != "yes":
        print("Bye!")
        break
