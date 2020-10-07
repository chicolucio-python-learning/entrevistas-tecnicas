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
    if not lst:
        raise ValueError('Empty list')
    return lst[-1], lst[0]


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
