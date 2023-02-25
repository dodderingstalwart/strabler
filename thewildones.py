#! /usr/bin/env python
# thewildone.py removes affiliate links

import webbrowser
import re

def main():
    web_store = []
    webg = []
    web_name = ''

   # User enters affiliate link 
    while web_name != 'q':
        web_name = input('Enter website or (q): ') 
        if (web_name != 'q'):
            web_store.append(web_name)
        
        a = re.search("^http(s?):*", web_name)
        # remove '?' and everything to the right
        if a:
            for x in web_store:
                k = re.split("\?", x)
                webg.append(k[0])
        else:
            web_store.pop()
            continue

        print('**', ' ', k[0])
    
    # Output clean website
    print()
    print('*', '\n* '.join(set(webg)))

# call for main 
if __name__ == '__main__':
    main()
