birthYear = input("Enter the year you are born:")
print(type(birthYear))
print(type(bool(birthYear)))
age = 2023 - int(birthYear)
print(type(float(age)))
print("You are "+ str(age) +"y of age")

""" when you take the input you are basically 
taking the input in the form of a string 
so when we perform mathematical calculation 
int()
str()
float()
bool()"""