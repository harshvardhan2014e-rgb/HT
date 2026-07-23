import random
attemps_list = []
def show_score():
    if len(attemps_list) <= 0:
     print("There is no High score, it's yours for the taking")
    else:
     print("The current high score is {} attemps".format(min(attemps_list)))
def start_game():
    random_number = int(random.randint(1, 10))
    print("Hey there! welcome to the the game of guesses!")
    player_name = ("Hi whats is your name: ")
    wanna_play = input("Hi, {}, would you like to play the guessing game? (Yes/No)"
    .format(player_name))
    attemps = 0
    show_score()
    while wanna_play.lower() == "yes":
        try:
            guess = input("Pick A number between 1 and 10")
            if int(guess) < 1 or int(guess) > 10:
               raise ValueError("Please enter within the given range")
            if int(guess) == random_number:
                print("Congrats! you guessed it right")
            attemps += 1
            attemps_list.append(attemps)
            print("it Took you {} attemps.".format(attemps))
            play_again = input("Would you like to play again? (Yes/No)")
            attemps = 0
            show_score()
            random_number = int(random.randint(1, 10))
            if play_again.lower() == "no":
                print("That's Cool")
                break
            elif int(guess) < random_number:
             print("it's Lower")
             attemps += 1
            elif int(guess) > random_number:
               print("its's Higher")
               attemps += 1
        except ValueError as err:
           print("Its not a vaild  input")
           print("{}".format(err))
    else:
       print("Thats cool")
if __name__ == '__main__':
  start_game


