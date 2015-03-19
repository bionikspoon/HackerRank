def purchasing_power((money, price, deal)):
    quantity = money // price
    wrappers = quantity
    while wrappers >= deal:
        bonus, wrappers = divmod(wrappers, deal)
        quantity += bonus
        wrappers += bonus

    return quantity


def main(_input):
    _ = _input.pop(0)

    result = [purchasing_power(map(int, line.split())) for line in _input]
    return map(str, result)


if __name__ == "__main__":
    from fileinput import input

    def get_input():
        return [line for line in input()]

    solution = main(get_input())
    print "\n".join(solution)
