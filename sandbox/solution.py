def insertion_sort(l):
    for i in xrange(1, len(l)):
        key = l[i]
        if key < l[i-1]:
            l[i] = l[i-1]
            l[i] = key
        print l



def main():
    _ = input()
    ar = [int(i) for i in raw_input().strip().split()]
    insertion_sort(ar)
    print " ".join(map(str, ar))
    pass


if __name__ == "__main__":
    main()