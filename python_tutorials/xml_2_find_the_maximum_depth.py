from fileinput import input
from xml.etree import ElementTree as ET

depth = 0


def get_input():
    data = [line for line in input()][1:]
    return "".join(data)


def get_items(element, count):
    global depth
    depth = max(depth, count)
    return [get_items(item, count + 1) for item in element if
            element is not None]


def main(input_data):
    global depth
    root = ET.fromstring(input_data)
    get_items(root.iter(), 0)
    return depth - 1


if __name__ == "__main__":
    print main(get_input())
