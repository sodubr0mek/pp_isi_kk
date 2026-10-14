n = input("Your number: ")
try:
    n = int(n)
except:
    print("Provided number is not an integer")
else:
    if n >= 0:
        factorial = 1
        for i in range(n):
            factorial = factorial * (n-i)
        print(n, "! = ", factorial, sep='')
    else:
        print("Provided number is negative")