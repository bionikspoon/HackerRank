from cmath import sqrt


def is_fibo(number):
    pre = 5 * number ** 2
    pos = sqrt(pre + 4)
    neg = sqrt(pre - 4)
    return pos.real.is_integer() or neg.real.is_integer()


def main():
    n = int(input())
    for _ in xrange(n):
        print 'IsFibo' if is_fibo(int(input())) else 'IsNotFibo'


if __name__ == "__main__":
    main()
