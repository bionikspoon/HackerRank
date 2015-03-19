def hunt_treasure((n, a, b)):
    left = [i * a for i in xrange(n - 1, 0 - 1, -1)]
    right = [i * b for i in xrange(n)]
    result = {l + r for l, r in zip(left, right)}
    return " ".join(map(str, sorted(result)))


def main(_input):
    _input = map(int, _input)
    t = _input.pop(0)

    return [hunt_treasure(_input[i * 3:i * 3 + 3]) for i in xrange(t)]


if __name__ == "__main__":
    from fileinput import input

    print "\n".join(main([_line for _line in input()]))
