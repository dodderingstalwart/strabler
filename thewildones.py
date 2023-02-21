#! /usr/bin/env python
# thewildone removes affiliate links

import webbrowser
import re
#import pyperclip

def main():
    web_site1 = []
    web_name = ''
    
    while web_name != 'q':
        web_name = input('Enter website address or q to quit: ') 
        if web_name != 'q':
            web_site1.append(web_name)
    # remove '?' and everything to the right
    for x in web_site1:
        k = re.split("\?", x)
        print('*','Output Address: ',k[0])

# call for main 
if __name__ == '__main__':
    main()
