a = input("First number: ")
b = input("Second number: ")
sign = input("Operation (+, -, *, /, //, %, **): ")

if a.isdigit() == 0:
    print("Error: The first number is not a number")
elif a.isdigit() == 0:
    print("Error: The second number is not a number")
elif sign not in ["+", "-", "*", "/", "//", "%", "**"]:
    print("Error: Unrecognisable operation")
elif sign in ["/", "//", "%"] and int(b) == 0:
    print("Error: Division by zero")
else:
    a = int(a)
    b = int(b)
    if sign == "+":
        c = a + b
    elif sign == '-':
        c = a - b
    elif sign == '*':
        c = a * b
    elif sign == '/':
        c = a / b
    elif sign == '//':
        c = a // b
    elif sign == '%':
        c = a % b
    elif sign == '**':
        c = a ** b

    print(a, sign, b, "=", c)