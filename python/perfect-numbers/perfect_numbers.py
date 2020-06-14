from functools import reduce
from math import sqrt


def _get_factors(n):
    step = 2 if n % 2 else 1
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if not n % i)))


def _cmp(a, b):
    '''
    Compare two numbers and return -1 if 'b' is smaller, 0 if equal and 1
    if greater than `a`
    '''
    return (a > b) - (a < b)


Classification = {
    -1: "deficient",
    0: "perfect",
    1: "abundant",
}


def classify(number):
    if number < 1:
        raise ValueError("Passed argument is not a natural number")

    aliquot_sum = sum(_get_factors(number)) - number

    return Classification[_cmp(aliquot_sum, number)]
