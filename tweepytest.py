#!/usr/bin/python3
"""
Testing for tweepy import
"""
import sys

if __name__ == '__main__':
    modulename = 'tweepy'

    if modulename not in sys.modules:
        print('You have not imported the {} module'.format(modulename))
