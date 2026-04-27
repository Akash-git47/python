a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))
c = int(input("Enter the third number :"))
d = b**2 - 4*a*c
if d > 0:
    root1 = (-b + d**0.5) / (2*a)
    root2 = (-b - d**0.5) / (2*a)
    print("The roots are real and distinct : ", root1, "and", root2)
elif d == 0:
    root = -b / (2*a)
    print("The roots are real and equal : ", root)