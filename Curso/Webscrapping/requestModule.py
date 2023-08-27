#! /usr/bin/env python3
import requests, os

dir_path = os.path.dirname(os.path.realpath(__file__))
res=requests.get('http://automatetheboringstuff.com/files/rj.txt')
print('Status of the GET is %d'%res.status_code)
print('Length of the text importes is %d'%len(res.text))
print(res.text[0:500])

res.raise_for_status() #This will raise an exception on a bad import


#badres=requests.get('http://automatetheboringstuff.com/files/asdfasdfas234234')
#badres.raise_for_status() #Stops and raise an exception 
RJfile=os.path.join(dir_path,'RomeoandJuliet.txt')
playFile=open(RJfile,'wb') #open a file in write binary mode to keep the Unicode formatting of the downloaded text

#Content method returns chunks on content of args lenght in bytes
for chunk in res.iter_content(100000): 
    playFile.write(chunk)

