#! /usr/bin/env python
# thewildone.py removes affiliate links

import webbrowser
import re

def main():
    web_site1 = []
    web_name = ''
    
    while web_name != 'q':
        web_name = input('Enter website address or q to quit: ') 
        if (web_name != 'q'):
            web_site1.append(web_name)
        
        a = re.search("^http*", web_name)
        # remove '?' and everything to the right
        if a:
            for x in web_site1:
                k = re.split("\?", x)
                print('*','Output Address: ',k[0])
        else:
            print("Enter address starting with http")
            continue

# call for main 
if __name__ == '__main__':
    main()
