salary = int(input("Enter the salary :"))
if salary < 10000:
    print("The bonus is : ", salary * 0.1)
elif salary >= 10000 and salary < 20000:
    print("The bonus is : ", salary * 0.15)
else:
    print("The bonus is : ", salary * 0.2)