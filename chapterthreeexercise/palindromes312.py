number = int(input("enter any five numbers you like: "))

if 10000 <= number <= 99999:
    first_digit = number // 10000
    second_digit = (number // 1000) % 10
    fourth_digit = (number // 10) % 10
    fifth_digit = number % 10

    if first_digit == fifth_digit and second_digit == fourth_digit:
        print("palindrome.")
    else:
        print("not  palindrome")
else:
    print("Invalid,enter five numbers.")
