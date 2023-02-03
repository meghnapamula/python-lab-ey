#!/usr/bin/python3


def evens(n):
    '''
    Returns a list of even numbers from 0 to n inclusive.
    '''
    xs = range(n)

    def even(xs):
        if n % 2 == 0:
            return n
        else:
            return ''
    xs = filter(even, xs)
    xs = list(xs)
