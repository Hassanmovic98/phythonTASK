amount= float(input('how much is your total spending:'))


if amount >= 1000 and amount <= 10000: 
	print('congratulations,you are to receive 5%')

elif amount >= 10000 and amount <= 51000:
	print('congratulations,you are to receive 10%')

elif amount > 50000:
	print('congratulations,you are to receive 20%')
elif amount <1000:	
	print('sorry,not qualified for discount')


"""
Ask user amount they have spent on purchase
if user  expenses is greater than 1k and also less than 10k,they should receive 5%
if user  expenses is greater than 10k and also less than 50k,they should receive 10%
if user  expenses is greater than 50k user should receive 20%  
if user expenses is less than 1k they are not qualified joor 
"""