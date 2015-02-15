from fileinput import input


def get_input():
    return [int(line) for line in input()][0]


# noinspection PyPep8Naming
def F():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


if __name__ == '__main__':
    n = get_input()
    a = F()
    sequence = [a.next() for _ in xrange(n)]
    print map(lambda x: x ** 3, sequence)