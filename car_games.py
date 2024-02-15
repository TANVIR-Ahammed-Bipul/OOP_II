print("This is a car game. If you don't know the mechanism then, type 'help'.")
choice=""
while True:
    choice=input("Enter mechanism: ")
    if choice=="start":
        print("Car Started.")

    elif choice=="stop":
        print("Car Stopped.")

    elif choice=="help":
        print("start-> For starting car")
        print("stop-> For stop the car")
        print("quit-> Playing Stopped")

    else:
        break

else:
    print("I don't Understand. Enter correct command.")