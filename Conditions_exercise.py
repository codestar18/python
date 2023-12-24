temperature = int(input("Enter the temperature in celcius:"))
if temperature>=30:
    print("It's a hot day")
elif temperature<20:
    print("It's a cold day")
elif temperature == 25:
    print("It's a mild hot day")
else:
    print("It's neither hot nor cold")