i = 0
while i<3:
    user_inp = input("Guess the number:")
    if(int(user_inp) == 8):
        print("You Win!")
        break
    elif int(user_inp) != 8 and i<2:
        print("Try once more")
    else:
        print("You lost")
    i = i+1
else:
    print("your chances are over")

#While loop also have else clause like if
#it will get executed when while loop fails
