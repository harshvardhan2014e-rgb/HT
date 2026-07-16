file_read = open('codingal2.txt', 'r')
print("File in read mode -")
print(file_read.read())
file_read.close()

file_write = open('codingal2.txt', 'w')
file_write.write("File in write mode ....")
file_write.write("Hi! i am Penguin. I am 1 yr. old")
file_write.close()

file_append = open('codingal2.txt', 'a')
file_append.write("\n File in Append mode....")
file_append.write("Hi! i am Penguin. I am 1 yr. old")
file_append.close()