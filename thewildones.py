#! /usr/bin/env python
# thewildone removes affiliate links

import webbrowser
import re
#import pyperclip
#import sys

# Main Title of program
#def title():
    #print("The Wild Ones".center(50, '*'))
    #print(''.center(50 ,'*'))

# Retriving an affiliate link website address
#def getWebsite():
    #webSite = input('Enter website: ')
    #return webSite

def main():
    web_site1 = []
    #if (len(sys.argv)) < 1:
        #print('Enter a valid website address')
    #web_site1 = sys.argv[1]
    web_name = ''
    #title()
    #web_site2 = getWebsite()
    #web_site1 = input('Enter Website Address: ')
    while web_name != 'quit':
        web_name = input('Enter a website address: ') 
        if web_name != 'quit':
            web_site1.append(web_name)

    for x in web_site1:
        k = re.split("\?", x)
        print('Output Address: ',k[0])

# call for main 
if __name__ == '__main__':
    main()
