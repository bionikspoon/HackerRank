def utopian_tree(cycles):
    height = 0
    for i in xrange(cycles + 1):
        if i % 2 == 1:
            height *= 2
        else:
            height += 1
    return height


def main(input_data):
    input_data = [str(utopian_tree(int(item))) for item in
                  input_data.split("\n")[1:]]

    return "\n".join(input_data)


if __name__ == "__main__":
    from fileinput import input

    def get_input():
        return "\n".join([line.strip() for line in input()])

    print main(get_input())
