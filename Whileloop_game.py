
command = ""
has_started= False
has_stopped = True


""" here while True means the loop runs until 
it breaks explicitly in the condition i.e user enters 
quit"""
while True:
    command = input(">").lower()

    if command == 'start':

        if has_started:
            print("Car is already started!!")
        else:
            has_started = True
            print("Ready to go....")

    elif command == 'stop':
        if has_stopped and not has_started:
            print("Car is not started! pls start the car")
        elif has_started and has_stopped:
            print("Car Stopped")
            has_stopped = False
        elif not has_stopped:
            print("Car stopped Already")

    elif command == 'help':
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == 'quit':
        break
    else:
        print("Sorry, I don't understand")
