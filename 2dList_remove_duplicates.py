numbers = [2, 4, 8, 1, 9, 4, 8]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)