
try:
    age = int(input("Age:"))
    income = 20000
    risk = income/age
    print(age)
    print(risk)

except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Cannot divide by 0")

'''except Exception: #we can use ValueError being specific
    print("Invalid input")'''