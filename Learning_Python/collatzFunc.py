
def collatz():
	global number
	if number % 2 == 0:
		number = number // 2
		print(number)
		return number

	else:
		number = number * 3 + 1
		print(number)
		return number

print('Please enter a number for the Collatz sequence:')
number = int(input())
while number != 1:
	

	collatz()
