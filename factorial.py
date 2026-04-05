num = int(input("Enter a numbr :"))
factorial = 1 
if num < 0:
    print("Factorial of negative numbner does not exist :")
elif num == 0 :
    print("Fatorial of 0 is 1 :")
else:
    for i in range(1,num +1):
        factorial = factorial * i 
    print("Factorial of ",num,"is ",factorial)