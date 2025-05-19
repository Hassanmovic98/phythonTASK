"""
(Table of Squares and Cubes) In Exercise 2.8, you wrote a script to calculate the
squares and cubes of the numbers from 0 through 5, then printed the resulting values in
table format. Reimplement your script using a for loop and the f-string capabilities you
learned in this chapter to produce the following table with the numbers right aligned in
each column.
 """
hassan = int(input("Enter any digit to calculate square and cubes: "))

print("number\tsquare\tcube")

for number in range(hassan + 1):
    print(number, "\t", number**2, "\t", number**5)