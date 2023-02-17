#! /usr/bin/env python
# thewildone removes affiliate links

import webbrowser
import re
#import pyperclip

# Main Title of program
def title():
    print("The Wild Ones".center(50, '*'))
    print(''.center(50 ,'*'))

# Retriving an affiliate link website address
def getWebsite():
    webSite = input('Enter website: ')
    return webSite

def main():
    title()
    webSite = getWebsite()
    x = re.split("\?", webSite)
    k = x[0]
    del webSite
    #pyperclip.pbcopy(k)
    print('')
    print(k)

if __name__ == '__main__':
    main()
