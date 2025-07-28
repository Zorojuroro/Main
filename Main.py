num1 = int(input("enter your 1st number: "))
op = input("select an operator (+ - * /): ")
num2 = int(input("enter your seond number: "))

if  op ==  "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
elif op == "":
    print("enter an operator")
else:
    print(f"{op} is not a valid operator")