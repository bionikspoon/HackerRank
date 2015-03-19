# coding=utf-8
def insertion_sort(l):
    l_copy = l[:]
    for i in xrange(1, len(l)):
        assert len(l[:i]) == len(l_copy[:i])
        assert l[:i] == sorted(l_copy[:i])
        j = i - 1
        key = l[i]
        while (l[j] > key) and (j >= 0):
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key
        assert l[:i + 1] == sorted(l_copy[:i + 1])


out = lambda x: ' '.join(map(str, x))


def main():
    m = input()
    ar = [int(i) for i in raw_input().strip().split()]
    insertion_sort(ar)
    print out(ar)


if __name__ == "__main__":
    main()
