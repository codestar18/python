name = input("Enter your name:")
length = len(name);
print(length)
if length<3:
    print("Name must be at least 3 characters")
elif length>50:
    print("Name can be maximum of 50 characters")
else:
    print("Name looks good !")