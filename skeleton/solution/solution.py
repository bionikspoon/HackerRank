def main(_input):
    _ = _input.pop()

    result = _input
    return map(str, result)


if __name__ == "__main__":
    from fileinput import input

    def get_input():
        return [line for line in input()]

    print "\n".join(main(get_input()))
