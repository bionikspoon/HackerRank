def maximize_xor(l, r):
    max_xor = 0
    for a in xrange(l, r + 1):
        for b in xrange(a, r + 1):
            max_xor = max(max_xor, a ^ b)
    return max_xor


def main(input_data):
    l, r = [int(item) for item in input_data.split("\n")[:2]]

    return maximize_xor(l, r)


if __name__ == "__main__":
    from fileinput import input

    def get_input():
        return "\n".join([line.strip() for line in input()])

    print main(get_input())
