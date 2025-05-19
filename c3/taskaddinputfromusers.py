number = int(input("enter any five numbers you like: "))

if number < 1 or number > 10000:
            print("invalid enter number between 1 to 10000")
total = 0
while number > 0:
            remainder = number % 10
            total += remainder
            number = number // 10

print("Sum of digits:", total)

 
    

 

