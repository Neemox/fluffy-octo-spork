### this program says hello and asks for my name
print('Hello World!')
print('What is your name?')  #asks for the users name as input
myName = input()
print('It is good to meet you,  ' + myName)
print('Your name has ' + str(len(myName)) + ' letters in it.')
print('What is your current age?') # asks for the users age as an input
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')