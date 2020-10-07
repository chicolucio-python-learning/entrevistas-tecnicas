from collections import deque
from itertools import chain, cycle


def zip_longest(n, n2, fillvalue):  # defining our own zip_longest
    n = list(n)
    n2 = list(n2)
    minor, greater = sorted([n, n2], key=len)
    minor_with_fillvalues = chain(minor, cycle([fillvalue]))
    return zip(greater, minor_with_fillvalues)


def less_to_great_significant_digit(s):
    return map(int, reversed(s))


def binary_sum(n, n2):
    """
    n and n2 are non negative binary numbers with arbitrary len. Ex:
    '00010101001010101010101010101010101001010101010101010'

    Consider that the limit for integers is 2^63 - 1
    """

    n = less_to_great_significant_digit(n)
    n2 = less_to_great_significant_digit(n2)
    last_d_sum = 0
    result = deque()
    for d, d2 in zip_longest(n, n2, fillvalue=0):
        d_sum = last_d_sum + d + d2
        last_d_sum = 0 if d_sum < 2 else 1
        result.appendleft(str(d_sum % 2))
    if last_d_sum == 1:
        result.appendleft('1')
    return ''.join(result)


def test_binary_sum():
    assert binary_sum('111110', '1100') == '1001010'


def test_less_digit():
    assert list(less_to_great_significant_digit('111110')) == [0, 1, 1, 1, 1, 1]
