#! /usr/bin/env python
# thewildone removes affiliate links

import webbrowser
import re

def title():
    print("The Wild Ones".center(50, '*'))
    print(''.center(50 ,'*'))

def main():
    title()
    webSite = input('Enter website: ')
    x = re.split("\?", webSite)
    k = x[0]
    del x
    print('')
    print(k)

if __name__ == '__main__':
    main()
