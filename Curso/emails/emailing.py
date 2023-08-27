#! /usr/bin/env python3
import smtplib

conn=smtplib.SMTP('smtp.gmail.com',587) #Connect to gmail server
type(conn)

conn.ehlo() #This is the first handshake
conn.starttls() #This encripts messages

conn.login('jimvillarene@gmail.com','zhxeuvmgjfevhpsp')#Login into the server, you need the app password from Google Account>security>Verififación en dos pasos>app password
conn.sendmail('jimvillarene@gmail.com','jimvillarene@gmail.com','Subject: Hello this is the subject\n\nDear me, so long \nand thanks for all the fish\n\n-Rene') #sender email, recipient email

conn.quit()