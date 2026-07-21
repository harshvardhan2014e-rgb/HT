new_file = open('text2.txt', 'x')
new_file.close()

import os
print("Checking if my_file exits or not.......")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("the file Does not exits")

my_file = open("my_file.txt", "w")
my_file.write("Hi! I am Penguin and i am 1yr old.")
my_file.close()

os.remove('text2.txt')
os.rmdir('Folder')