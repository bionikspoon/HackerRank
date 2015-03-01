def main():
    n = int(raw_input())
    an = map(int, raw_input().split())
    n -= 1
    v = an[n]
    out = lambda(x): ' '.join(map(str, x))
    while an[n - 1] > v and n > 0:
        an[n] = an[n - 1]
        n -= 1
        print out(an)
    else:
        an[n] = v
        print out(an)


if __name__ == "__main__":
    main()