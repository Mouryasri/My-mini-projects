print("---Mini Calculator---")

Number1 = float(input("Enter first number: "))
Number2 = float(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
Choice = int(input("Enter your choice: "))
if Choice == 1:
    print(Number1+Number2)
elif Choice == 2:
    print(Number1-Number2)
elif Choice == 3:
    print(Number1*Number2)
elif Choice == 4:
    print(Number1/Number2)
else:
    print("Invalid input")