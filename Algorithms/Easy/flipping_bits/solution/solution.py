def main(input_data):
    input_data = [str(bin(int(item))[2:]).zfill(32) for item in
                  input_data.split("\n")[1:]]
    input_data = [item.replace('1', '5').replace('0', '1').replace('5', '0') for
                  item in input_data]

    input_data = map(lambda x: int(x, 2), input_data)
    return "\n".join(map(str, input_data))


if __name__ == "__main__":
    from fileinput import input

    def get_input():
        return "\n".join([line.strip() for line in input()])

    print main(get_input())
