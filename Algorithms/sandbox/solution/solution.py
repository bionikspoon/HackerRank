def main(input_data):
    input_data = input_data.split("\n")
    return sum(map(int, input_data))


if __name__ == "__main__":
    from fileinput import input

    def get_input():
        return "\n".join([line.strip() for line in input()])

    print main(get_input())
