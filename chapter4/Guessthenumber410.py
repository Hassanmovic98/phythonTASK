import random
number = random.randint(1,1000)


guess =int(input("Guess my number between 1 and 1000 with the fewest guesses: "))


if guess == number:
	print("Congratulations. You guessed the number")


elif guess > number:
	print("Your guess is too high")
elif guess < number:
	print("Your guess is too low")



 


