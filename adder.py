##adder.py
total = 0
for num in range(101):
	total = total + num
	if total < 1000:
		continue
	print(total)
print(total)