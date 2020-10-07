import random
import pytest


def max_min(lst):
    """
    Calculate the maximum and minimum of a list lst

    Parameters
    ----------
    lst : list

    Returns
    -------
    tuple
        (max, min)
    """
    n = len(lst)
    if n == 0:
        raise ValueError('Empty list')

    max_value = min_value = lst[-1]

    def max_min_rec(cursor):
        """

        Parameters
        ----------
        cursor : int

        Returns
        -------
        tuple
        """
        nonlocal max_value, min_value
        if cursor < 0:
            return max_value, min_value
        current = lst[cursor]
        if current > max_value:
            max_value = current
        if current < min_value:
            min_value = current
        return max_min_rec(cursor - 1)

    return max_min_rec(n-1)


def test_error():
    lst = []
    with pytest.raises(ValueError):
        max_min(lst)


def test_single_element_list():
    lst = [1]
    assert max_min(lst) == (1, 1)


def test_ordered_list():
    lst = list(range(0, 11))
    assert max_min(lst) == (10, 0)


def test_random_list():
    lst = list(range(100))
    random.seed(42)
    random.shuffle(lst)
    assert lst[0] == 42
    assert lst[-1] == 81
    assert max_min(lst) == (99, 0)