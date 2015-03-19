import itertools


def cavity_conditions((i, j), cavity_map):
    cell = cavity_map[j][i]
    adjacent_cells = [cavity_map[n + j][m + i] for (m, n) in
                      [(-1, 0), (1, 0), (0, 1), (0, -1)]]

    return cell > max(adjacent_cells)


def main():
    n = int(input())

    cavity_map = [list(str(input())) for _ in xrange(n)]

    cavities = [(i, j) for i, j in itertools.product(xrange(1, n - 1), repeat=2)
                if cavity_conditions((i, j), cavity_map)]
    for (i, j) in cavities:
        cavity_map[j][i] = 'X'
    print '\n'.join([''.join(map(str, cavities)) for cavities in cavity_map])


if __name__ == "__main__":
    main()