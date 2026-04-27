amount = float(input("Enter purchase amount: "))

if amount >= 5000:
    discount = 0.20
elif 2000 <= amount < 5000:
    discount = 0.10
else:
    discount = 0

final_amount = amount - (amount * discount)

print("Final amount after discount:", final_amount)
