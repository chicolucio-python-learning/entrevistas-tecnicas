BLACK = 'B'
WHITE = 'W'
EMPTY = 'E'


def has_move(board, line, column):
    """Given a board with Black, White and Empty slots, This functions must
    calculate if starting from line and column defined as parameters there are
    empty slots that can be occupied.
    Imagine each player start with a position occupied. So the first can occupy
    any adjacent Empty slot. After that the second player can do the same and
    so on until there is no more Empty slot adjacent to any occupied one.
    :param board: Matrix m x n
    :param line: The line of start slot
    :param column: The column of start slot
    :return: True if there is any Empty slot adjacent
    """
    m = len(board)

    if m == 0:
        raise Exception('Board must have at least one line')
    n = len(board[0])
    if n == 0:
        raise Exception('Board must have at least one column')

    color = board[line][column]
    if color == EMPTY:
        raise Exception('Initial position can not be empty')

    def adjacents(position):
        def interval(value, value_max):
            return range(max(value - 1, 0), min(value + 2, value_max))

        p_line, p_column = position
        line_interval = interval(p_line, m)
        column_interval = interval(p_column, n)

        return [(l, c) for l in line_interval for c in column_interval]

    def has_empty_adjacent(position):
        return any(board[p_line][p_column] == EMPTY for p_line, p_column in adjacents(position))

    def adjacents_with_same_color(position):
        return [(l, c) for l, c in adjacents(position) if color == board[l][c]]

    to_be_visited = {(line, column)}
    visited = set()

    while len(to_be_visited) > 0:
        current_position = to_be_visited.pop()
        if has_empty_adjacent(current_position):
            return True
        visited.add(current_position)
        for p in adjacents_with_same_color(current_position):
            if p not in visited:
                to_be_visited.add(p)
    return False


board_white_unfinished = [
    [EMPTY, WHITE, BLACK, EMPTY],
    [EMPTY, WHITE, BLACK, EMPTY],
    [EMPTY, WHITE, BLACK, EMPTY],
    [EMPTY, WHITE, BLACK, EMPTY]
]
board_white_finished = [
    [WHITE, WHITE, BLACK, BLACK],
    [WHITE, WHITE, BLACK, BLACK],
    [WHITE, WHITE, BLACK, BLACK],
    [WHITE, WHITE, BLACK, EMPTY]
]


def test_unfinished():
    assert has_move(board_white_unfinished, 1, 1)


def test_finished():
    assert has_move(board_white_finished, 0, 3)
    assert not has_move(board_white_finished, 1, 1)
