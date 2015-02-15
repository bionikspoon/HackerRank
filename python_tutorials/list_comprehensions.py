def calculate_coordinates(x, y, z, n):
    """
    >>> calculate_coordinates(1,1,1,2)
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
    >>> calculate_coordinates(2,2,2,2) # doctest: +NORMALIZE_WHITESPACE
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0,
    0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2,
    0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1],
    [2, 2, 2]]
    """

    result = [[i, j, k]
              for i in range(x + 1)
              for j in range(y + 1)
              for k in range(z + 1)
              if i + j + k != n]
    return result


if __name__ == '__main__':
    input_x, input_y, input_z, input_n = (
        int(raw_input()), int(raw_input()), int(raw_input()), int(raw_input()))
    print calculate_coordinates(input_x, input_y, input_z, input_n)
