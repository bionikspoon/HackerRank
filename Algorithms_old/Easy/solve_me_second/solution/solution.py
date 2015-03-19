def main(input_data):
    input_data = [map(int, item.split(" ")) for item in
                  input_data.split("\n")[1:]]
    return "\n".join(map(str, [a + b for (a, b) in input_data]))


if __name__ == "__main__":
    from fileinput import input

    def get_input():
        return "\n".join([line.strip() for line in input()])

    print main(get_input())
