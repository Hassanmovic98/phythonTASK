import random

frequency1= 0
frequency2 = 0
frequency3 = 0
frequency4 = 0
frequency5 = 0
frequency6 = 0
frequency7 = 0
frequency8 = 0
frequency9 = 0
frequency10 = 0

for roll in range( 10_000_000):
	face = random.randrange (1, 10)



if face == 1:
	frequency1 += 1
elif face == 2:
	frequency2 += 1
elif face == 3:

	frequency3 +=1
elif face == 4:
	frequency4
elif face == 5:
	frequency5 +=1
elif face == 6:
	frequency6 +=1
elif face == 7:
	frequency7 +=1
if face == 8:
	frequency8 +=1
if face == 9:
	frequency9 +=1
if face == 10:
	frequency10 +=1

print(f'{"Face":>4}{"frequency":>15}')
print(f'{1:>4}{"frequency1":>15,}')
print(f'{2:>4}{"frequency2":>15,}')
print(f'{3:>4}{"frequency3":>15,}')
print(f'{4:>4}{"frequency4":>15,}')
print(f'{5:>4}{"frequency5":>15,}')
print(f'{6:>4}{"frequency6":>15,}')
print(f'{7:>4}{"frequency7":>15,}')
print(f'{8:>4}{"frequency8":>15,}')
print(f'{9:>4}{"frequency9":>15,}')
print(f'{10:>4}{"frequency10":>15,}')


