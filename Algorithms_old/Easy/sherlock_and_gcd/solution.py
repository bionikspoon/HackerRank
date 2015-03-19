from fractions import gcd


def not_gcd(haystack):
    needle = reduce(gcd, haystack)
    return 'YES' if needle == 1 else 'NO'


def main(_input):
    t = int(_input.pop(0))

    return [not_gcd(map(int, _input[i + 1].split())) for i in
            xrange(0, t * 2, 2)]


if __name__ == "__main__":
    from fileinput import input

    print "\n".join(main([_line for _line in input()]))
