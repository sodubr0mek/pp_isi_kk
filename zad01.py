name = input("Name: ")
year = input("Year of birth: ")

if year.isdigit() == 0:
    print("Error: The year is not a digit")
elif int(year) < 1900 or int(year) > 2026:
    print("Error: The year is not in range")
else:
    print("Hello, ", name, "! You are " , 2026-int(year) , " years old.", sep='')

    say = "Hello, {0}! You are {1} years old."
    print(say.format(name, 2026-int(year)))