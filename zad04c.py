a = input("Enter the first number:")
b = input("Enter the second number:")

try:
    a = int(a)
    b = int(b)
except:
    print("Error: One of provided numbers is not an integer")
else:
    if a >= b:
        print("Error: The first number must be greater than the second")
    else:
        for i in range(b - a + 1):
            if (a + i) % 2 == 1:
                print(a + i, end=' ')
            else:
                continue
        print("")
        for i in range(b - a + 1):
            if (a + i) % 3 == 0:
                print(a + i, end=' ')
            else:
                continue
        print("")