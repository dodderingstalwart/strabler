#! /usr/bin/env python
# thewildone.py removes affiliate links

import webbrowser
import re

def main():
    web_site1 = []
    webg = []
    web_name = ''
    
    while web_name != 'q':
        web_name = input('Enter website address or q to quit: ') 
        if (web_name != 'q'):
            web_site1.append(web_name)
        
        a = re.search("^http(s?)*", web_name)
        # remove '?' and everything to the right
        if a:
            for x in web_site1:
                k = re.split("\?", x)
                webg.append(k[0])
        else:
            web_site1.pop()
            continue

        print('**', ' ', k[0])
        
    print('*', ' ', webg)

# call for main 
if __name__ == '__main__':
    main()
