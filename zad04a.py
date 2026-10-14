a = input("First number: ")
b = input("Second number: ")

try:
    a = int(a)
    b = int(b)
except:
    print("Error: One of the provided numbers is not an integer")
else:
    for i in range(a):
        for j in range(b):
            print(i + 1, "*", j+1, "=", (i+1)*(j+1))