largest = 0
second_largest = 0
number = 0

while number <= 10:
    number =float(input("enter number: "))

if number > largest:
	second_largest = largest
	largest = number

       
elif number > second_largest:
	second_largest = number
		

print(f"The largest number is: {largest}")
print(f"The second largest number is: {second_largest}")
