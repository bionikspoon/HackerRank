import string

letters = {v: k for k, v in enumerate(string.lowercase)}


def std(func):
    def wrapper(_input):
        _input = [item for item in _input.split("\n")[1:]]
        _result = func(_input)
        return "\n".join(map(str, _result))

    return wrapper


def palindrome_maker(word):
    global letters

    count = 0

    for i in xrange(len(word)):
        left, right = letters.get(word[i]), letters.get(word[-i - 1])
        if left > right:
            count += left - right

    return count


@std
def main(input_data):
    return [palindrome_maker(word) for word in input_data]


if __name__ == "__main__":
    from fileinput import input

    def get_input():
        return "\n".join([line.strip() for line in input()])

    print main(get_input())
