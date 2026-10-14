p = input("Number of points: ")

try:
    p = int(p)
except:
    print("Error: Number provided is not an integer")
else:
    match p:
        case n if n <= 49:
            print("ndst")
        case n if n >= 50 and n <= 59:
            print("dst")
        case n if n >= 60 and n <= 69:
            print("dst plus")
        case n if n >= 70 and n <= 79:
            print("db")
        case n if n >= 80 and n <= 89:
            print("db plus")
        case n if n >= 90 and n <= 100:
            print("bdb")
        case _:
            print("Error: Some error has happened")

