#! /usr/bin/env python3
import re
namesRegex=re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob'))
#With sub you subsitute
print(namesRegex.sub('REDACTED','Agent Alice gave the secret documents to Agent Bob')) #Will substitute the regular expresion with the word REDACTED
#Just giving away a little bit of the original Regex
namesRegex=re.compile(r'Agent (\w)\w*') #One word character and the all the other characters *=zero or more
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob'))
print(namesRegex.sub(r'Agent \1*****','Agent Alice gave the secret documents to Agent Bob')) #Will substitute the regular expresion with the word REDACTED

#Verbose allows for format to add comments and spaces to make it readable
re.compile(r'''
(\d\d\d-)|       #area code without parenthesis
(\(\d\d\d\) )   #area code with parens
-               #first dash
\d\d\d
-
\d\d\d\d
''', re.VERBOSE)
