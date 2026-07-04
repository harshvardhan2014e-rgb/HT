def disarium():
    num = int(input("Enter a number: "))
    original = num
    total = 0
    power = len(str(num))

    while num > 0:
        digit = num % 10
        total += digit ** power
        power -= 1
        num //= 10

    if total == original:
        print("Disarium Number")
    else:
        print("Not a Disarium Number")

disarium()

   