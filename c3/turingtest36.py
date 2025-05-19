"""
Create a script that plays the part of the independent computer, giving its user a sim
ple medical diagnosis. The script should prompt the user with 'What is your problem?'
 When the user answers and presses Enter, the script should simply ignore the user’s input,
 then prompt the user again with 'Have you had this problem before (yes or no)?' If
 the user enters 'yes', print 'Well, you have it again.' If the user answers 'no', print
 'Well, you have it now.'
 Would this conversation convince the user that the entity at the other end exhibited
 intelligent behavior? Why or why not?
|"""

print('welcome to Hassan medical diagnosis')

question1 = input("Hello,what is your problem?: ")

choice = input('Have you had this problem before? enter  for yes and  for no: ')


if choice == 'yes':
	print("well,you have it again")
elif choice == 'no':
	print("well,you have it now")
else : 
	print("please you have to pick from the right choice which is either yes 1 or no 2")