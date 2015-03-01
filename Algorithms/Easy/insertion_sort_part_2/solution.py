def insertion(an, n, out):
    v = an[n]
    while an[n - 1] > v and n > 0:
        an[n] = an[n - 1]
        n -= 1
    else:
        an[n] = v
        print out(an)


def main():
    n = int(raw_input())
    an = map(int, raw_input().split())
    n -= 1
    out = lambda (x): ' '.join(map(str, x))
    for i in range(1, n + 1):
        insertion(an, i, out)


if __name__ == "__main__":
    main()