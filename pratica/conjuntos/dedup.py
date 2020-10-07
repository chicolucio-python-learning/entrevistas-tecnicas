def dedup(lst):
    """Remove duplicates from lst"""
    result = []
    repeated = set()

    for element in lst:
        if element not in repeated:
            result.append(element)
            repeated.add(element)
    return result


def test_dedup():
    lst = ['banana', 'banana', 'banana', 'abacaxi', 'caqui']
    assert dedup(lst) == ['banana', 'abacaxi', 'caqui']