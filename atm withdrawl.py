account_balance = int(input("Enter the account balance :"))
withdrawl_amount = int(input("Enter the withdrawl amount :"))
if withdrawl_amount < 100:
   print("Transaction Failed : Minimum withdrawl amount is 500")
elif withdrawl_amount > 10000:
    print("Transaction Failed : Maximum withdrawl amount is 10000")
else:
    print("Withdrawl successful")
    