#! /usr/bin/env python

def mainTitle():
    print('************The Wild Ones************')


def main():

    mainTitle()

    # Make a dict() for every character
    leads = {"biker" : "Johnny", "rival" : "Chino", "lady" : "Kathie"}

    for l, k in leads.items():
        print('\t', l, ':', k)


if __name__ == '__main__':
    main()

