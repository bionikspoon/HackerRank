# coding=utf-8
def main():
    n = int(input())
    ar = map(int, raw_input().split())
    n -= 1
    v = ar[n]
    out = lambda x: ' '.join(map(str, x))
    while n > 0 and ar[n - 1] > v:
        ar[n] = ar[n - 1]
        n -= 1
        print out(ar)
    else:
        ar[n] = v
        print out(ar)


if __name__ == "__main__":
    main()
