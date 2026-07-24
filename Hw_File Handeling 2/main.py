with open("Text.txt", "w") as f:
    f.write("Hi! I am a Student at Codingal. My name is Harsh. I am 12 yrs old.")

with open("Text.txt", "a") as f:
    f.write("\nFile in append mode....")
    f.write("\nHi! I am a Student at Codingal. My name is Harsh. I am 12 yrs old.")

with open("Text.txt", "r") as f:
    print("File in read mode...")
    print(f.read())

with open("codingal2.txt", "w") as f:
    f.write("File in write mode ....\n")
    f.write("Hi! I am Penguin. I am 1 yr old.")

with open("codingal2.txt", "a") as f:
    f.write("\nFile in append mode....")
    f.write("\nHi! I am Penguin. I am 1 yr old.")


with open("codingal2.txt", "r")as f:
    print("File in read mode....")
    print("Hi! I am Penguin. I am 1 yr old.")

with open("Text.txt", "r") as f:
    lines = f.readlines()
    print("\nWords in this file are:")
    for line in lines:
        print(line.split())

with open("codingal2.txt", "r") as f:
    lines = f.readlines()
    print("\nWords in this file are:")
    for line in lines:
        print(line.split())
