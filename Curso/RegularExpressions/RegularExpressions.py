#! /usr/bin/env python3
import re
lyrics="""[Verse 1]
On the first day of Christmas, my true love sent to me
A partridge in a pear tree

[Verse 2]
On the second day of Christmas, my true love sent to me
Two turtle doves, and
A partridge in a pear tree

[Verse 3]
On the third day of Christmas, my true love sent to me
Three french hens
Two turtle doves, and
A partridge in a pear tree

[Verse 4]
On the fourth day of Christmas, my true love sent to me
Four calling birds
Three french hens
Two turtle doves, and
A partridge in a pear tree

[Verse 5]
On the fifth day of Christmas, my true love sent to me
Five golden rings
Four calling birds
Three french hens
Two turtle doves, and
A partridge in a pear tree

You might also like

Did you know that there’s a tunnel under Ocean Blvd
Lana Del Rey

Castles Crumbling (Taylor’s Version) [From The Vault]
Taylor Swift

Timeless (Taylor’s Version) [From The Vault]
Taylor Swift

[Verse 6]
On the sixth day of Christmas, my true love sent to me
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves, and
A partridge in a pear tree

[Verse 7]
On the seventh day of Christmas, my true love sent to me
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves, and
A partridge in a pear tree

[Verse 8]
On the eighth day of Christmas, my true love sent to me
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves, and
A partridge in a pear tree


[Verse 9]
On the ninth day of Christmas, my true love sent to me
Nine ladies dancing
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves, and
A partridge in a pear tree

[Verse 10]
On the tenth day of Christmas, my true love sent to me
Ten lords a-leaping
Nine ladies dancing
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves, and
A partridge in a pear tree

[Verse 11]
On the eleventh day of Christmas, my true love sent to me
Eleven pipers piping
Ten lords a-leaping
Nine ladies dancing
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves, and
A partridge in a pear tree


[Verse 12]
On the twelfth day of Christmas, my true love sent to me
12 drummers drumming
11 pipers piping
10 lords a-leaping
9 ladies dancing
8 maids a-milking
7 swans a-swimming
6 geese a-laying
5 golden rings
4 calling birds
3 french hens
2 turtle doves, and
1 partridge in a pear tree"""

xmasRegex=re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))

vowelRegex=re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food'))

doublevowelRegex=re.compile(r'[aeiouAEIOU]{2}')
print(doublevowelRegex.findall('Robocop eats baby food'))

consonantRegex=re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('Robocop eats baby food'))


input()
