def hanoi(n, orig='A', aux='B', dest='C'):
    """Recursive solution to Hanoi Tower"""
    if n >= 1:
        hanoi(n-1, orig, dest, aux)
        print(f'{orig} -> {dest} : {n}')
        hanoi(n-1, aux, orig, dest)


for i in range(1, 4):
    print(f'\n#### Hanoi {i}')
    hanoi(i)
