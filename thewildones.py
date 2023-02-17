#! /usr/bin/env python
# thewildone removes affiliate links

import webbrowser
import re
#import pyperclip
import sys

# Main Title of program
def title():
    print("The Wild Ones".center(50, '*'))
    print(''.center(50 ,'*'))

# Retriving an affiliate link website address
#def getWebsite():
    #webSite = input('Enter website: ')
    #return webSite

def main():
    if (len(sys.argv)) < 1:
        print('Enter a valid website address')
    web_site1 = sys.argv[1]
    title()
    #web_site2 = getWebsite()
    x = re.split("\?", web_site1)
    k = x[0]
    del web_site1
    #pyperclip.pbcopy(k)
    print('')
    print(k)
    exit()

if __name__ == '__main__':
    main()
