import random

while True:
    choiceToPick = ["rock","paper","scissors"]
    computer = random.choice(choiceToPick)
    player = None

    while player not in choiceToPick:
        player = input("rock, paper, scissors?: ").lower()

        if player == computer:
            print("Computer Picked: ",computer)
            print("Player Picked: ", player)
            print("It is a Tie!!")
        elif player == "paper":
            if computer == "scissors":
                print("Computer Picked: ",computer)
                print("Player Picked: ", player)
                print("You lose this round!!")
            if computer == "rock":
                print("Computer Picked: ",computer)
                print("Player Picked: ", player)
                print("You win this round!!")
        elif player == "rock":
            if computer == "paper":
                print("Computer Picked: ",computer)
                print("Player Picked: ", player)
                print("You lose this round!!")
            if computer == "scissors":
                print("Computer Picked: ",computer)
                print("Player Picked: ", player)
                print("You win this round!!")
        elif player == "scissors":
            if computer == "rock":
                print("Computer Picked: ",computer)
                print("Player Picked: ", player)
                print("You lose this round!!")
            if computer == "paper":
                print("Computer Picked: ",computer)
                print("Player Picked: ", player)
                print("You win this round!!")

    playAgain = input("Will you like to play again? (Yes/No): ").lower()

    if playAgain != "yes":
        break
    
print("See you Next time!!")