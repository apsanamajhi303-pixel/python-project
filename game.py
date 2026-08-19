import random
#---Baner---
print("*"*30)
print("ROCK - PAPER - SCISSORS")
print("*"*30)

#---SETUP---
choices = ("rock", "paper", "scissors")
beats = {
    "rock": "scissors",  
    "scissors": "paper",
    "paper": "rock"
}
score = {"players": 0, "computer": 0, "ties": 0}

#GAME LOOP------
playing = True
while playing:
    player_choice = input("\n Enter your choice (rock, paper, scissors): ").lower().strip()
    print(player_choice)
    while player_choice not in choices:
        player_choice = input("\n Invalid choice. Please enter rock, paper, or scissors: ").lower().strip()
    computer_choice = random.choice(choices)
    print(f"\n Computer choice: {computer_choice}")
    if player_choice == computer_choice:
        print("It's a tie!")
        score["ties"] += 1
    elif beats[player_choice] == computer_choice:
        print("You win!")
        score["players"] += 1
    else:
        print("Computer wins!")
        score["computer"] += 1
    print(f"Score -> you: {score['players']} | computer: {score['computer']} | ties: {score['ties']}")

    again = input("Do you want to play again? (y/n):").lower().strip()
    if again != "y":
        playing = False

    print("\n Thanks for playing! Final Score ->")
    print(score)