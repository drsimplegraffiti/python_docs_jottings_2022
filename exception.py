while True:
    try:
        x = int(input("Please enter a number: "))
        if (x < 0):
            print("Please enter a number more than 0")
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
