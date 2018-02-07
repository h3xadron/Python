#!/bin/python
#code=utf-8


name = input('What is your name?: ')
age = int(input('How old are you?: '))
year = str(2018+(100-age))
print(name + ' you will be 100 years old ' + year)
answare = input("Would you like contineu? y/n ")
while answare == "y":
	num = int(input('Give me a new number! '))
	result = str(2018+(100-num))
	print(result)
	answare = input("And now? y/n ")

exit