def isInt(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

spam = ''
while True:
	##print('what is spam?')
	spam = input('What is spam? ')
	if isInt(spam) and int(spam) == 1:
		print('Hello!')
		continue
	if isInt(spam) and int(spam) == 2:
			print('Howdy')
			continue
	else:
		print('Greetings!')
		break