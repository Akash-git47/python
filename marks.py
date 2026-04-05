marks = float(input("Enter your marks : "))
if marks <0 or marks > 100:
    print("Invalid marks")
elif marks >= 85:
    print("A")
elif marks >=70 and marks <85:
    print("B")
elif marks >=60 and marks <70:
    print("C")
elif marks >=45 and marks <60:
    print("D")
else:
    print("Fail")
