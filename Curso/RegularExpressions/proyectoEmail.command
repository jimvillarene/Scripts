#! /usr/bin/env python3
import re, pyperclip
# Create our Regexobject for phone numbers
phoneRegex= re.compile(r'''
#415-555-0000, 555-0000, (415) 555-0000, 555-00000 ext. 12345, x12345 - question mark is optional (0 or more times)
(
((\d\d\d)|(\(\d\d\d\)))?  #area code optional
(\s|-)                    #first separator
\d\d\d                    #first 3 digits
-                         #second separator
\d\d\d\d                  #last 4 digits
(((ext(\.)?\s)|x)          #optional extension word part
 (\d{2,5}))?                 #optional extension number part
 )                         #We get it in a large group to avoid different groups from messing the looks of the phone numbers, the first item will be the good phone number
''',re.VERBOSE)
#Create a REgex object for email adresses
emailRegex=re.compile(r'''
#some.+_thing@something.com
[a-zA-Z0-9._,+]+ #name part, on square brackets we dont need to backslash the special characters
@               #add symbol
[a-zA-Z0-9._,+]+  #domain part
''',re.VERBOSE)
#Get the text off the clipboard
text=pyperclip.paste()
#Extract the email addresses and phone numbers from text
extractedPhone=phoneRegex.findall(text)
#Create a list to save the first items of the phone numbers and append the first item of each tuple
allPhoneNumbers=[]
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])
    
extractedEmail=emailRegex.findall(text)
#Print results for debugging
#print(extractedEmail)
#print(extractedPhone)
#print(allPhoneNumbers)

#Copy the extracted email andphone numbers to the clipboard
# We will use join to put all phone numbers separated with a new line character '\n'
results='\n'.join(allPhoneNumbers)+'\n'+'\n'.join(extractedEmail)
# print(results) #Debugging print
pyperclip.copy(results)
