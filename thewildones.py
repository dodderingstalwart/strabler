#! /usr/bin/env python
# thewildone.py removes affiliate links and only affiliate links

import webbrowser
import re
import sys

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
            # Does not work with youtube link
            clean_link = re.search("^http(s?):*", web_name)
            if clean_link:
                for x in web_store:
                    k = re.split("\?", x)
                    web_fixed.append(k[0])
            # pop the last 'q' off the stack
            else:
                if web_store:
                    web_store.pop()
                    continue
                else:
                    sys.ext("No website entered")

            print('***', ' ', k[0])
    
    # Output clean website
    print()
    print('\n** '.join(set(web_fixed)))

# call for main 
if __name__ == '__main__':
    main()
