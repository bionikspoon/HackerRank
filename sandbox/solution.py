def main():
    (n, m) = map(int, raw_input().split(' '))
    a = map(int, raw_input().split(' '))
    b = map(int, raw_input().split(' '))
    c = map(int, raw_input().split(' '))

    for i in range(10**9+7):
        for j in range(n):
            if j % b[i] == 0:
                a[j] *= c[i]
    print ' '.join(map(str, a))


if __name__ == "__main__":
    main()