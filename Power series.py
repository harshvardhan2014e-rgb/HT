n = int(input("Enter the number of terms: "))

for i in range(1, n + 1):
    term = i ** i

    print(term, end=" ")
