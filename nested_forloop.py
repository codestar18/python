numbers = [5,2,5,2,2]

for j in numbers:
    print("x"*j)

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output +='x'
    print(output)