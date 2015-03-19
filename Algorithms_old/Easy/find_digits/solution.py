def find_digits(number):
    return sum([number.count(digit) for digit in set(number) if
                int(digit) > 0 and int(number) % int(digit) == 0])


def main():
    n = int(input())
    for _ in xrange(n):
        print find_digits(str(input()))


if __name__ == "__main__":
    main()
