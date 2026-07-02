# Dictionary provided
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Ask user for a key
key = int(input(" Enter a key (1-6): "))

# Check if the key exists in the dictionary
if key in d:
    print("The value is:", d[key])
else:
    print("Key not found")
