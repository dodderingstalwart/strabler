#! /usr/bin/env python

class Person():
    def __init__(self, name, job):
        self.name = name
        self.job = job

def mainTitle():
    title = 'The Wild Ones'
    print(''.rjust(20, '*'), title, ''.ljust(20, '*'))

def main():

    mainTitle()
    leader = Person('Johnny', 'biker')
    rival = Person('Chino', 'biker')
    watress = Person('Kathie', 'watress')

    # Make a dict() for every character
    leads = {"biker" : "Johnny", "rival" : "Chino", "lady" : "Kathie"}

    for l, k in leads.items():
        print('\t', l.center(30).rstrip(), ':', k)

    print("\nSelect character to get their information: ")


if __name__ == '__main__':
    main()
