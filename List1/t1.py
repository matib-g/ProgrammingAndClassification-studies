while True:
    try:
        x = int(input("Enter your number: "))
    except ValueError:
        print("This number is not an integer. Try again.")
        continue
    else:
        if x % 2 == 0:
            print("Your number is even.")
        else:
            print("Your number is odd.")
