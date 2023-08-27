#! /usr/bin/env python3
import re
beginswithHelloRegex=re.compile(r'^Hello')
print(beginswithHelloRegex.search('Hello there!'))
print(beginswithHelloRegex.search('Hey!!Hello there!'))


endswithWorldRegex=re.compile(r'World$')
print(endswithWorldRegex.search('Hello World'))
print(endswithWorldRegex.search('Hello World!!!!'))

allDigitsRegex=re.compile(r'^\d+$')
print(allDigitsRegex.search('12342135346345342'))
print(allDigitsRegex.search('1234213sdf5346345342'))

atRegex=re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat'))

atRegex=re.compile(r'.{1,2}at')
print(atRegex.findall('The cat in the hat sat on the flat mat'))

print('First Name: Al Last Name:Dweigart'.find(':'))
print('First Name: Al Last Name:Dweigart'.find(':')+2)
print('First Name: Al Last Name:Dweigart'[12:])

nameRegex=re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall('First Name: Al Last Name:Dweigart'))

nongreedy=re.compile(r'<(.*?)>')
print(nongreedy.findall('<To serve humans> for dinner.>'))

greedy=re.compile(r'<(.*)>')
print(nongreedy.findall('<To serve humans> for dinner.>'))

prime='Serve the public trust.\nProtect the innocent.\n Upload the law'
print(prime)

dotStar=re.compile(r'.*')
print(dotStar.search(prime))

dotStar=re.compile(r'.*',re.DOTALL)
print(dotStar.search(prime))

vowelRegex=re.compile(r'[aeiou]')
print(vowelRegex.search('Al, Why does your programming book talk about RoboCop so much'))
print(vowelRegex.search('Al, Why does your programming book talk about RoboCop so much'),re.I)
input()
