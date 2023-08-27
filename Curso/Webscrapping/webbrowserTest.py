#! /usr/bin/env python3
import webbrowser, sys, pyperclip

sys.argv #Here it receives arguments from the command line
if len(sys.argv)>1: #Check if the script receives arguments
    address=' '.join(sys.argv[1:])
else:
    address=pyperclip.paste()    
#check if we're receiving

webbrowser.open('https://www.google.com/maps/place/' + address)