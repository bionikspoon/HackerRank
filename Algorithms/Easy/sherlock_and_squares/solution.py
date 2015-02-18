from math import sqrt


def count_squares((left, right)):
    left = int(sqrt(left-1))
    right = int(sqrt(right))
    return right - left


def main(_input):
    _ = _input.pop(0)

    result = [count_squares(map(int, case.split())) for case in _input]
    return map(str, result)


if __name__ == "__main__":
    from fileinput import input

    def get_input():
        return [line for line in input()]

    solution = main(get_input())
    print "\n".join(solution)
