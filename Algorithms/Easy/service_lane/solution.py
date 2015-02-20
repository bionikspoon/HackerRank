def main():
    (n, t) = map(int, raw_input().split(' '))
    width = map(int, raw_input().split(' '))
    for _ in xrange(t):
        (i, j) = map(int, raw_input().split(' '))
        print min(width[i:j + 1])


if __name__ == "__main__":
    main()