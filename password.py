password = (input('please enter your password:'))
length = len(password)

if length > 0 and length < 8:
	print('too weak')

elif length == 8:
	print(' still weak but go ahead')

elif length > 8 and length <= 16:
	print('now its strong')

elif length > 16:
	print ('strong enough')