#! /usr/bin/env python3

import shelve

shelfFile=shelve.open('mydata')
shelfFile['cats']=['Zophie','Pooka','Fat-tail','Cleo']
shelfFile.close()

shelfFile=shelve.open('mydata')
shelfFile['cats']
shelfFile.close()
