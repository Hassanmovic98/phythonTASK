first = float(input("Enter first number: "))
second = float(input("Enter second number: "))
third= float(input("Enter third number: "))

if first <= second and second <= third:
    print(first, second, third)
elif first <= second and third <= second:
    print(first, third, second)
elif second <= first and first <= third:
    print(second, first, third)
elif second <= third and third <= first:
    print(second, third, first)
elif third <= first and first <= second:
    print(third, first, second)
else:
    print(third, second, first)
