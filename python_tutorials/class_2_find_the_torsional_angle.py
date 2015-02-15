from math import acos, degrees, sqrt


class Vector(object):
    def __init__(self, coordinates):
        self.coordinates = map(float, coordinates)

    def __sub__(self, other):
        (x1, y1, z1) = self.coordinates
        (x2, y2, z2) = other.coordinates
        return Vector((x1 - x2, y1 - y2, z1 - z2))

    @staticmethod
    def dot(a, b):
        (x1, y1, z1) = a.coordinates
        (x2, y2, z2) = b.coordinates

        return sum((x1 * x2, y1 * y2, z1 * z2))

    @staticmethod
    def cross(a, b):
        (x1, y1, z1) = a.coordinates
        (x2, y2, z2) = b.coordinates
        i = y1 * z2 - z1 * y2
        j = -1 * (z1 * x2 - x1 * z2)
        k = x1 * y2 - y1 * x2
        return Vector((i, j, k))

    @staticmethod
    def arccos(number):
        return acos(number)

    @staticmethod
    def degrees(number):
        return degrees(number)

    @property
    def norm(self):
        return sqrt(sum(map(lambda x: x * x, self.coordinates)))


# noinspection PyPep8Naming
def main(input_data):
    A, B, C, D = [Vector(line.split(" ")) for line in input_data.split("\n")]
    BA, BC, DC = (B - A), (B - C), (D - C)
    x, y = Vector.cross(BA, BC), Vector.cross(BC, DC)
    numerator = Vector.dot(x, y)
    denominator = x.norm * y.norm
    result = Vector.degrees(Vector.arccos(numerator / denominator))

    return "%.2f" % result


if __name__ == "__main__":
    from fileinput import input

    def get_input():
        return "\n".join([line.strip() for line in input()])

    print main(get_input())


