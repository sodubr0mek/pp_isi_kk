p = input("Number of points: ")

try:
    p = int(p)
except:
    print("Error: Number provided is not an integer")
else:
    if p > 100 or p < 0:
        print("Error: points out of range")
    else:
        if p >= 0 and p <= 49:
            print("ndst")
        elif p >= 50 and p <= 59:
            print("dst")
        elif p >= 60 and p <= 69:
            print("dst plus")
        elif p >= 70 and p <= 79:
            print("db")
        elif p >= 80 and p <= 89:
            print("db plus")
        elif p >= 90 and p <= 100:
            print("bdb")

        

