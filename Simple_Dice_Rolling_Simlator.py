import random

def roll_dice():
    sides = [1, 2, 3, 4, 5, 6]
    return random.choice(sides)

def play_simulator():
    while True:
        choice = input("Roll the dice? (yes/no): ").lower().strip()
        
        if choice == "yes" or choice == "y":
            result = roll_dice()
            print(f"You rolled a: {result}")
        elif choice == "no" or choice == "n":
            print("Thank you for playing!")
            break
        else:
            print("Invalid input. Please enter yes or no.")

if __name__ == "__main__":
    play_simulator()
