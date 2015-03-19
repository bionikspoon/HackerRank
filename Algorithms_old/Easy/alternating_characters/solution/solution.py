from re import findall


def std(func):
    def wrapper(_input):
        _input = [item for item in _input.split("\n")[1:]]
        _result = func(_input)
        return "\n".join(map(str, _result))

    return wrapper


def alternating_characters(word):
    return sum(map(lambda x: len(x) - 1, findall(r'AA*|BB*', word)))


@std
def main(input_data):
    return [alternating_characters(word) for word in input_data]


if __name__ == "__main__":
    from fileinput import input

    def get_input():
        return "\n".join([line.strip() for line in input()])

    print main(get_input())
