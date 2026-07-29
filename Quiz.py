class QuizProgram:
    def __init__(self):
        self.score = 0

    def start_quiz(self):
        print("Welcome to General knowledge quiz\n")

        print("1. what is the capital of india?\n(a) delhi\n(b) mumbai\n(c) kolkata")
        answer1 = input("answer: ")
        if answer1 == "a":
            print("correct\n")
            self.score += 1
        else:
            print("wrong, the answer was a\n")

        print("2. who painted the mona lisa?\n(a) leonardo da vinci\n(b) pablo picasso\n(c) vincent van gogh")
        answer2 = input("answer: ")
        if answer2 == "a":
            print("correct\n")
            self.score += 1
        else:
            print("wrong, the answer was a\n")

        print("3. which planet is called the red planet?\n(a) mars\n(b) jupiter\n(c) venus")
        answer3 = input("answer: ")
        if answer3 == "a":
            print("correct\n")
            self.score += 1
        else:
            print("wrong, the answer was a\n")

        print("4. How many continents are there?\n(a) 5\n(b) 6\n(c) 7")
        answer4 = input("answer: ")
        if answer4 == "c":
            print("correct\n")
            self.score += 1
        else:
            print("wrong, the answer was c\n")

        print("5. What is the largest ocean?\n(a) atlantic\n(b) pacific\n(c) indian")
        answer5 = input("answer: ")
        if answer5 == "b":
            print("correct\n")
            self.score += 1
        else:
            print("wrong, the answer was b\n")

        self.show_final_score()

    def show_final_score(self):
        print("---Quiz finished !---")
        print("score: " + str(self.score) + " out of 5")

if __name__ == "__main__":
    game = QuizProgram()
    game.start_quiz()
