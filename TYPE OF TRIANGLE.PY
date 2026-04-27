n1= int(input("Enter the first side of the triangle :"))
n2= int(input("Enter the second side of the triangle :"))
n3= int(input("Enter the third side of the triangle :"))
if n1==n2 and n2==n3:
    print("The triangle is equilateral")
elif n1==n2 or n2==n3 or n1==n3:
    print("The triangle is isosceles")
else:
    print("The triangle is scalene")