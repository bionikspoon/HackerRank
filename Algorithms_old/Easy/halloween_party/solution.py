def cut_chocolate(cuts):
    horizontal, vertical = divmod(cuts, 2)
    vertical += horizontal
    return horizontal * vertical


def main(_input):
    _ = _input.pop(0)

    result = [cut_chocolate(int(case)) for case in _input]
    return map(str, result)


if __name__ == "__main__":
    from fileinput import input

    def get_input():
        return [line for line in input()]

    solution = main(get_input())
    print "\n".join(solution)
