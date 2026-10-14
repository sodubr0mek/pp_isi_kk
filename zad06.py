def factorial_iter(m):
    if m >= 0:
        factorial = 1
        for i in range(m):
            factorial = factorial * (m-i)
        print(m, "! = ", factorial, sep='')
    else:
        print("Provided number is negative")


def factorial(m):
    if m > 0:
        return m * factorial(m-1)
    if m == 0:
        return 1
    print(factorial(n))


def fibonacci_iter(m):
    for i in range(m):
        if i == 0:
            u = 0
            r = 0
            f = 0
        r = u
        u = f
        if i == 0:
            f = 1

        f = f + r
        print(f," ",end='')
    if m == 0:
        print(0)

def fibonacci_rek(m):

    if m == 0:
        return 0
    elif m == 1:
        return 1
    else:
        return fibonacci_rek(m-1) + fibonacci_rek(m-2)

def gcd_iter(m, k):
    if m > k:
        p = m
        m = k
        k = p
    for i in range(k):
        if m % (i+1) == 0 and k % (i+1) == 0:
            anws = (i+1)
    return anws

def gcd_rek(m, k):
    return m if k == 0 else gcd_rek(k, m % k)
    
    