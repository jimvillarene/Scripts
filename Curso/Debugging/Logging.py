#! /usr/bin/env python3
import logging, os
print(os.getcwd())
filepath='/Users/albertorenejimenezvilla/Documents/Scripts/Curso/Debugging'
debugFile=os.path.join(filepath,'myProgramLog.txt')
logging.basicConfig(filename=debugFile ,level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s') #filename gets all the errors into a textfile
#logging.disable(logging.CRITICAL) #This one disables all logging, so commenting it out cleans all logging messages from critical to lower, othe levels are DEBUG, INFO, WARNING, ERROR, CRITICAL
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial %s' % (n))
    total=1
    for i in range (1,n+1):
        total*=i
        logging.debug('value of i %s , value of total %s' % (i,total))
    logging.debug('return value is %s' % (total))
    return total

print(factorial(5))
logging.debug('End of program')
