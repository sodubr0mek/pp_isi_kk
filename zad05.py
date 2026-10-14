import math
dziel = 0
n = int(input("Your number: "))


if n < 2:
    print("Error: number must be at least 2")
else:
    for i in range(math.isqrt(n)+1):
        if i == 0 or i == 1:
            continue
        if n % i == 0:
            dziel += 1
    if dziel == 0:
        print("This is a prime number")
    else:
        print("This is not a prime number")