from fileinput import input
from math import sqrt


class ComplexNumber(object):
    def __init__(self, a, b):
        self.a, self.b = round(float(a), 2), round(float(b), 2)

    def __str__(self):
        a = "" if self.a == 0 else "%.2f" % self.a
        b = " - %.2fi" % abs(
            self.b) if self.b < 0 else "" if self.b == 0 else " + %.2fi" % self.b
        b = b if self.a != 0 else "%.2fi" % self.b
        return "0.00" if self.a == self.b == 0 else "".join((a, b))

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return ComplexNumber(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        a, b, c, d = self.a, self.b, other.a, other.b
        return ComplexNumber(a * c - b * d, b * c + a * d)

    def __div__(self, other):
        a, b, c, d = self.a, self.b, other.a, other.b
        return ComplexNumber((a * c + b * d) / (c * c + d * d),
                             (b * c - a * d) / (
                                 c * c + d * d))

    def __abs__(self):
        return self.a ** 2 + self.b ** 2

    @property
    def mod(self):
        return "%.2f" % sqrt(abs(self))


def get_input():
    return [line.strip() for line in input()]


def main(input_data):
    input_data = [i.split(" ") for i in input_data]
    C, D = [ComplexNumber(i[0], i[1]) for i in input_data]
    return "\n".join(map(str, (
        C + D, C - D, C * D, C / D, C.mod, D.mod)))


if __name__ == "__main__":
    print main(get_input())
