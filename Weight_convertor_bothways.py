weight = float(input("Enter your Weight:"))
ch = input("Did you enter (L)bs or (K)g:")
if ch.upper() == 'L':
    converted_weight = weight*0.45
    print(f"{weight} pounds is {converted_weight} kg")
else:
    converted_weight = weight/0.45
    print(f"{weight} kg is {converted_weight} pounds")
