def inequity(_list, i, k):
    return _list[i + k - 1] - _list[i]


def main(n, k, candies):
    candies.sort()
    result = (inequity(candies, i, k) for i in xrange(n - k + 1))

    return str(min(result))


if __name__ == "__main__":
    def get_input():
        n = input()
        k = input()
        candies = [int(input()) for _ in xrange(n)]
        return n, k, candies

    _n, _k, _candies = get_input()
    print main(_n, _k, _candies)
