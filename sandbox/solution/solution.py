import string

letters = {v: k for k, v in enumerate(string.lowercase)}


def std(func):
    def wrapper(_input):
        _input = [int(item) for item in _input.split("\n")[1:]]
        _result = func(_input)
        return "\n".join(map(str, _result))

    return wrapper


def inequity(_list):
    return max(_list) - min(_list)


def list_mean(_list):
    return sum(_list) / len(_list)


def reduce_inequity(bundles, k):
    bundles = sorted(bundles)
    inequity_list = [(inequity(bundles[i:i + k]), list_mean(bundles[i: i + k]))
                     for i in xrange(len(bundles)-k)]

    mean = sorted(inequity_list, key=lambda (x, y): x)[0][-1]
    bundles = sorted(bundles, key=lambda x: abs(x - mean), reverse=True)
    return bundles[1:]


@std
def main(input_data):
    k = input_data.pop(0)
    for _ in xrange(len(input_data)-k):
        input_data = reduce_inequity(input_data, k)
    return [inequity(input_data)]


if __name__ == "__main__":
    from fileinput import input

    def get_input():
        return "\n".join([line.strip() for line in input()])

    print main(get_input())
