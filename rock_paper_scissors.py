import random

user_wins = 0
computer_wins = 0

options = ("rock", "paper", "scissors")

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()

    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    computer_pick = random.choice(options)

    if user_input == computer_pick:
        print("Tie")
    elif user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    else:
        print("Computer won!")
        computer_wins += 1


print(f"You won {user_wins} times.")
print(f"Computer won {computer_wins} times")