#rounding program very simple
print('Usage: Enter "round(number)"')
def round(number):
	myIntFloat = int(number)
	if number == myIntFloat:  ## if the number is already an integer, we don't need to round anything
		print(number)
	else:
		remainder = number - myIntFloat
		print('The remainder is ' + str(remainder) + ' .')  ## determine what the remainder of the number is using subtraction
		if remainder < 0.5: ## determine whether to round up or down.
			print('Which rounds down to ' + str(number - remainder))
		else :
			if remainder >= 0.5:
				print('Which rounds up to ' + str(int(number) + 1))
