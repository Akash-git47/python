# write a program to check weather an nnumber is divisiable by 5 and 11 or not
number = int(input("Enter a number :"))
if number % 5 ==0 and number % 11 ==0:
    print(number, "is divisible by 5 and 11 ")
else:
    print(number, "is not divisible by 5 and 11 ")
    