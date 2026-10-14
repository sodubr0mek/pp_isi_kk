tab = [1, 13, 15, 81, 7]

for i in range(len(tab)):
    count = 0
    for j in range(len(tab)):
        if tab[i] >= tab[j]:
            count += 1
        if count == len(tab):
            max = tab[i]

for i in range(len(tab)):
    count = 0
    for j in range(len(tab)):
        if tab[i] <= tab[j]:
            count += 1
        if count == len(tab):
            min = tab[i]
print(min)
print(max)
sum = 0
for i in range(len(tab)):
    sum = sum + tab[i]

mean = sum / len(tab)

print(sum)
print(mean)
