num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number : "))

numbers = [num1, num2, num3]

total_sum = 0
for n in numbers:
    total_sum = total_sum + n

product = 1
for n in numbers:
    product = product * n

smallest = numbers[0]
for n in numbers:
    if n < smallest:
        smallest = n

largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n

count = 0
for _ in numbers:
    count = count + 1

average = total_sum / count

print("\nResults:")
print("Sum:", total_sum)
print("Average:", average)
print("Product:", product)
print("Smallest:", smallest)
print("Largest:", largest)
