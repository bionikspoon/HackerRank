def has_sum_median(_list):
    left = 0
    right = sum(_list)
    for item in _list:
        right -= item
        if left == right:
            return True
        left += item
    return False


def main():
    t = int(input())
    for _ in xrange(t):
        _ = input()
        a = [int(i) for i in raw_input().split(' ')]
        print 'YES' if has_sum_median(a) else 'NO'


if __name__ == "__main__":
    main()