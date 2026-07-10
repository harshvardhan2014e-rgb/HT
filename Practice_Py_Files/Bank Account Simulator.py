balance = 1000

print("*******************************************")
print("Welcome to the Bank Account Simulator!")
print("*******************************************")

print("Your starting balance is: $", balance)

print("*******************************************")
print("BANK ACCOUNT SIMULATOR MENU")
print("*******************************************")

def menu():
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
menu()

choice = input("Enter your choice (1-4): ")

if choice == "1":
    deposit_amount = int(input("Enter the amount to deposit (Note: Please Don't Include Paise like 1000.00): "))
    balance += deposit_amount
    print("Deposit successful! New balance: $", balance)
    if deposit_amount > 10000:
        print("Note: Depositing more than $10,000 are not allowed. Please contact your bank for further assistance.")   

if choice == "2":
    withdraw_amount = int(input("Enter the amount to withdraw: "))
    if withdraw_amount < balance:
        balance - withdraw_amount
        print("Withdrawal successful! New balance: $", balance-withdraw_amount)
    else:
        print("Insufficient balance! Your current balance is: $", balance)

if choice == "3":
    print("Your current balance is: $", balance)

if choice == "4":
    print("********************************************")
    print("Thank you for using the Bank Account Simulator!")
    print("********************************************")



