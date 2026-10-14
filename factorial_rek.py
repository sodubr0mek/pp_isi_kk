n = input("Your number: ")
try:
    n = int(n)
except:
    print("Provided number is not an integer")
else:
    def factorial(m):
        if m > 0:
            return m * factorial(m-1)
        if m == 0:
            return 1
    print(factorial(n))