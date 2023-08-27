#! /usr/bin/env python3

'''

**********
*        *
*        *
*        *
**********


'''
import traceback

def boxprint(symbol,width,height):
    try:
        if len(symbol)!=1:
            raise Exception('"symbol" needs to be of a lenght of 1 character')
        if height<2 or width<2:
                raise Exception('width and height must be greater or equal to 2')
        print(symbol*width)
        for i in range(height -2):
            print(symbol+(' '*(width-2))+ symbol)
        print(symbol*width)
    except:
        errorFile=open('/Users/albertorenejimenezvilla/Documents/Scripts/Curso/Debugging/error_log.txt','a')
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print('The traceback info was written on error_log.txt')
    
    
boxprint('**',15,5)