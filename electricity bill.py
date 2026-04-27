n1 = int(input("Enter the first month :"))
n2 = int(input("Enter the number of units consumed :"))
if n1 == 1 or n1 == 2 or n1 == 3:
    if n2 <= 100:
        print("The electricity bill is : ", n2 * 4.5)
    elif n2 > 100 and n2 <= 200:
        print("The electricity bill is : ", (100 * 4.5) + (n2 - 100) * 6)
    else:
        print("The electricity bill is : ", (100 * 4.5) + (100 * 6) + (n2 - 200) * 10)