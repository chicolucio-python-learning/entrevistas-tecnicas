def phoneword(phonenumber):
    """Returns all possible phone words respective to a phone number
    :param phonenumber: str
    :return: list of str with all phone words
    """

    digit_to_chars = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    size = len(phonenumber)

    def phoneword_rec(previous_results, cursor):
        if cursor == size:
            return previous_results
        digit = phonenumber[cursor]
        results = []
        for char in digit_to_chars[digit]:
            results.extend(prev_result + char for prev_result in previous_results)
        return phoneword_rec(results, cursor + 1)

    return phoneword_rec([''], 0)


def test_empty():
    assert phoneword('') == ['']


def test_7():
    assert phoneword('7') == ['p', 'q', 'r', 's']


def test_73():
    assert phoneword('73') == ['pd', 'qd', 'rd', 'sd', 'pe', 'qe', 're', 'se', 'pf', 'qf', 'rf', 'sf']
