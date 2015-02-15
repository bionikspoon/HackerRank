def main(input_data):
    input_data = [map(int, item.split(" ")) for item in
                  input_data.split("\n")[1:]][0]

    return (item for item in input_data if input_data.count(item) == 1).next()


if __name__ == "__main__":
    from fileinput import input

    def get_input():
        return "\n".join([line.strip() for line in input()])

    print main(get_input())
