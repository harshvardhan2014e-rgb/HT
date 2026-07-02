def fib_series(nterms):
    n1, n2 = 0, 1
    count = 0
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1

nterms = int(input(" Enter the number of terms: "))

if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    fib_series(nterms)
else:
   print("Fibonacci Sequence:")
   fib_series(nterms)