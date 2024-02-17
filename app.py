#! /usr/bin/env python
# thewildone.py removes affiliate links and only affiliate links

import re
import sys
from flask import Flask
app = Flask(__name__)

@app.route('/')

def main():
    web_store = []
    web_fixed = []
    web_name = ''

   # Enter affiliate link 
    # replace nested loops to speed up
    while web_name != 'q':
        web_name = input('Enter website or non YouTube link or (q): ') 
        # check for 'ref' in link
        if (web_name != 'q'):
            web_store.append(web_name)
        
            # search and remove affilate link
            # Does not work with youtube link need to add 'ref' case
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
                # never hits this
                else:
                    sys.ext("No website entered")

            print('***', ' ', k[0])
    
    # Output website without link
    print()
    print('\n** '.join(set(web_fixed)))

# call for main 
if __name__ == '__main__':
    main()
