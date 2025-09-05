#! /usr/bin/env python
# thewildone.py removes affiliate links and only affiliate links

import re
import sys
from flask import Flask

app = Flask(__name__)

@app.route('/')
def remove_affiliate_links(url):
    # List of common affiliate parameters to remove from (claude ai)
    affiliate_params = [
        'ref', 'tag', 'aff', 'affiliate', 'utm_source', 'utm_medium', 'utm_campaign',
        'utm_term', 'utm_content', 'fbclid', 'gclid', 'mc_cid', 'mc_eid'
    ]

    # Split the URL into base and query parts
    if '?' in url:
        base_url, query_params = url.split('?', 1)

        # parse the query parameters
        params = query_params.split('&')
        filtered_params = []

        for param in params:
            if '=' in param:
                key, value = param.split('=')[0].lower()
                # Only keep parameters that are not in the affiliate list
                if not any(aff_param in key for aff_param in affiliate_params):
                    filtered_params.append(param)
        
        # Reconstruct the URL without affiliate parameters
        if filtered_params:
            return base_url + '?' + '&'.join(filtered_params)
        else:
            return base_url
    return url

def main():
    web_store = []
    web_fixed = []
    web_name = ''

    print("Strabler Application to remove affiliate links\n")
    print("*" * 40)
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
                    sys.exit("No website entered")

            print('***', ' ', k[0])
    
    # Output website without link
    print()
    print('\n** '.join(set(web_fixed)))

# call for main 
if __name__ == '__main__':
    # Check if running as web app or command line
    if len(sys.argv) > 1 and sys.argv[1] == 'web':
        app.run(debug=True)
    else:
        main()
