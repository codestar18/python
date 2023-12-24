matix = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
matix[0][1] = 2
print(matix[0][1])

for row in matix:
    for item in row:
        print(item,end = " ")
    print()