#! /usr/bin/env python

class Person():
    def __init__(self, name, job):
        self.name = name
        self.job = job

def mainTitle():
    print('************The Wild Ones************')

def main():

    mainTitle()
    rival = Person('Chino', 'biker')

    # Make a dict() for every character
    leads = {"biker" : "Johnny", "rival" : "Chino", "lady" : "Kathie"}

    for l, k in leads.items():
        print('\t', l, ':', k)


if __name__ == '__main__':
    main()
