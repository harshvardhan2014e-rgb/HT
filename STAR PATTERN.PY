# basic star pattern
print("Star pattern \n")
for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print('\n')
    
# Inverted  Star pattern
print("Inverted star pattern \n")
for i in range(6,1,-1):
   for j in range (1, 1, -1):
    print("*", end="")
    print('\n')
