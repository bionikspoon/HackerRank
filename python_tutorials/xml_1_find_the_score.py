from fileinput import input
from xml.etree import ElementTree as ET


def get_input():
    data = [line for line in input()][1:]
    return "".join(data)


def main(input_data):
    root = ET.fromstring(input_data)
    return sum([len(i.attrib) for i in root.iter()])


if __name__ == "__main__":
    print main(get_input())
