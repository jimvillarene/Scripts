#! /usr/bin/env python3
import os

totalsize=0

for filename in os.listdir('/Users/albertorenejimenezvilla/Documents/Scripts'):
    if not os.path.isfile(os.path.join('/Users/albertorenejimenezvilla/Documents/Scripts',filename)):
            continue
    totalsize=totalsize+os.path.getsize(os.path.join('/Users/albertorenejimenezvilla/Documents/Scripts',filename))
print(totalsize)



import os

print("Path at terminal when executing this file")
print(os.getcwd() + "\n")

print("This file path, relative to os.getcwd()")
print(__file__ + "\n")

print("This file full path (following symlinks)")
full_path = os.path.realpath(__file__)
print(full_path + "\n")

print("This file directory and name")
path, filename = os.path.split(full_path)
print(path + ' --> ' + filename + "\n")

print("This file directory only")
print(os.path.dirname(full_path))