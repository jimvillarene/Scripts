#! /usr/bin/env python3
import imapclient
conn=imapclient.IMAPClient('imap.gmail.com',ssl=True)
conn.login('jimvillarene@gmail.com','zhxeuvmgjfevhpsp') #Abrir el servidor IMAP con la contraseña de app
conn.select_folder('INBOX',readonly=True) #We get the Inbox folder
UIDs=conn.search(['TEXT', 'Welcome kit'])#IMAP passes a list of strings in a particular order
print(UIDs)
rawmessage=conn.fetch([41369],['BODY[]','FLAGS'])
print(rawmessage)
