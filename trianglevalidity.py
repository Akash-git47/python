n_1 = int(input("Enter the first side of teh triangle  :"))
n_2 = int(input("Enter the second side of the trinagle :"))
n_3 = int (input("Enter the third side of the triangle :"))
if n_1 + n_2 > n_3 and n_2 +n_3 > n_1 and n_1 +n_3 > n_2:
    print("The triangle is valide")
else:
    print("The triangle is not valide")