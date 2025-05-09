def countdown():
    while True:
        try:
            n = int(input("Enter a positive number: "))
            if n >= 1:
                break
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    for i in range(n, 0, -1):
        print(i)
    print("Blast off!")

# Run the program
countdown()