num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
num3 = int(input("enter third number"))
num4 = int(input("enter fourth number"))

sum = num1 + num2 +num3+num4
average = sum / 4
product = num1 * num2 * num3 * num4
lowest  = min(num1,num2,num3,num4)
highest = max (num1,num2,num3,num4)

print(f"the sum is {sum}")
print(f"the average of number is {average}")
print(f"the lowest number is {lowest}")
print(f"the highest number is {highest}")
