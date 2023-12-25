#we use to break our code
#we use def key word to define a function
#we can only use function below it, define funcs first and then define
#parameters are the placeholders that hold values passed to a func
#argument is the one we pass to name
#variables are the ones defined in the func or outside

def greet_user(name): #name is the parameter
    print(f"Hi {name}!!")
    print("Welcome abroad")


print("Start")
name = input("Enter your name:")
greet_user(name)
greet_user("Rakesh")#rakesh is the argument passed to parameter
#calc_cost(total=50,shipping=5, discount= 0.1)#passing arguments with their parameters = keyword argument
print("Finish")
#positional argument = passed in the order of parameters in the functions


