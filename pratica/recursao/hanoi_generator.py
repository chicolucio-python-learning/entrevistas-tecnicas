def hanoi(n, orig='A', aux='B', dest='C'):
    """Recursive solution to Hanoi Tower"""
    if n >= 1:
        yield from hanoi(n-1, orig, dest, aux)
        yield orig, dest, n
        yield from hanoi(n-1, aux, orig, dest)


def test_hanoi_1():
    g = hanoi(1)
    assert next(g) == ('A', 'C', 1)


def test_hanoi_2():
    g = hanoi(2)
    assert next(g) == ('A', 'B', 1)
    assert next(g) == ('A', 'C', 2)
    assert next(g) == ('B', 'C', 1)


def test_hanoi_3():
    g = hanoi(3)
    assert next(g) == ('A', 'C', 1)
    assert next(g) == ('A', 'B', 2)
    assert next(g) == ('C', 'B', 1)
    assert next(g) == ('A', 'C', 3)
    assert next(g) == ('B', 'A', 1)
    assert next(g) == ('B', 'C', 2)
    assert next(g) == ('A', 'C', 1)


if __name__ == '__main__':

    for i in range(1, 4):
        gen = hanoi(i)
        print(f'\n#### Hanoi {i}')
        for j in gen:
            print(f'{j[0]} -> {j[1]} : {j[2]}')
