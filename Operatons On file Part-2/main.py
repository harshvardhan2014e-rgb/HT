with open('TextFile.txt', 'w') as file:
    file.write("Hi! I am penguin and i am 1yr Old")
file.close()

with open('TextFile.txt', 'r') as file:
    data = file.readlines()
    print("Words in this file are.....")
    for line in data:
        word = line.split()
        print (word)
file.close()