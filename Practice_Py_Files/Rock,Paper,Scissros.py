import random


choices = ["Rock", "Paper", "Scissros"]

Playchoices = input("Enter Choices(Rock,Paper,Scissros) : ")


intplay = Playchoices

computer = random.choice(choices)

print("computer Choice=", computer)
print("Your Choice=", intplay)

if computer == intplay:
    print("Draw!")

if intplay == "Rock" and computer == "Scissros":
    print("You Win!")

if intplay == "Paper" and computer == "Rock":
    print("You Win!")

if intplay == "Scissros" and computer == "Paper":
    print("You Win!")


if computer == "Rock" and intplay == "Scissros":
    print("Computer Won")

if computer == "Paper" and intplay == "Rock":
    print("Computer Won!")

if computer == "Scissros" and intplay == "Paper":
    print("Computer Won!")









