Subject1 = int(input("Enter marks for Subject 1: "))
Subject2 = int(input("Enter marks for Subject 2: "))
Subject3 = int(input("Enter marks for Subject 3: "))
Subject4 = int(input("Enter marks for Subject 4: "))
Subject5 = int(input("Enter marks for Subject 5: "))

Total= Subject1 + Subject2 + Subject3 + Subject4 + Subject5

Average = Total / 5

print("Total Marks: ", Total)
print("Average Marks: ", Average)

if Average >= 90:
    print("Excellent")

elif Average >= 80:
    print("Good")

elif Average >= 50:
    print("Pass")

elif Average < 50:
    print("Below Average")
    