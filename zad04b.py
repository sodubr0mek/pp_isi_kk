sum = 0
while(True):
    a = input(":")
    try:
        a = int(a)
    except:
        print("Error: Number provided is not an integer")
        break
    else:
        if a != 0:
            sum = sum + a
        if a == 0:
            break
print("Sum:", sum)

