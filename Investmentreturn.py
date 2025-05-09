p = 1000
r = 0.07
years = [10, 20, 30]

amounts = [p * (1 + r) ** n for n in years]
print(amounts)
