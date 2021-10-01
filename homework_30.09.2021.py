import random

games_library = {1: "Rock", 2: "Paper", 3: "Scissors"}
player_score = 0
computer_score = 0

while player_score < 3 and computer_score < 3:

    print("Enter 1 for Rock, 2 for Paper and 3 for Scissors ")

    player_input = int(input(" Your turn: "))
    computer_input = random.randint(1, 3)

    print(str(games_library[player_input]) + " vs " + str(games_library[computer_input]))

    if player_input == 1 and computer_input == 3 or player_input == 2 and computer_input == 1 or player_input == 3 and computer_input == 2:
        player_score += 1
        print(str(player_score) + ":" + str(computer_score))

    elif computer_input == 1 and player_input == 3 or computer_input == 2 and player_input == 1 or computer_input == 3 and player_input == 2:
        computer_score += 1
        print(str(player_score) + ":" + str(computer_score))

    else:
        print("Draw")

if player_score == 3:
    print("You won!")
else:
    print("Computer wins!")