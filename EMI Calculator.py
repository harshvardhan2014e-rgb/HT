Loan_Amount = int(input("Hello! Please Enter Your Loan Amount: "))
Interest_Rate = int(input("Enter Interest Rate (%): "))
Timeperiod = int(input("Enter Time (months): "))

Years = Timeperiod / 12

Interest = (Loan_Amount * Interest_Rate * Years) / 100

Total = Loan_Amount + Interest

EMI = Total / Timeperiod

print("Interest =", Interest)
print("Monthly Payment =", EMI)