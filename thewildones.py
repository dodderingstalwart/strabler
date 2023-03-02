#! /usr/bin/env python
# thewildone.py removes affiliate links

import webbrowser
import re

def main():
    web_store = []
    web_fixed = []
    web_name = ''

   # User enters affiliate link 
    while web_name != 'q':
        web_name = input('Enter website or (q): ') 
        if (web_name != 'q'):
            web_store.append(web_name)
        
        # search and remove affilate link
        clean_link = re.search("^http(s?):*", web_name)
        if clean_link:
            for x in web_store:
                k = re.split("\?", x)
                web_fixed.append(k[0])
        else:
            web_store.pop()
            continue

        print('***', ' ', k[0])
    
    # Output clean website
    print()
    print('**', '\n* '.join(set(web_fixed)))

# call for main 
if __name__ == '__main__':
    main()
