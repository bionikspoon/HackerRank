# coding=utf-8
out = lambda x: ' '.join(map(str, x))


def quicksort(haystack):
    needle = haystack.pop(0)
    l = []
    r = []
    for item in haystack:
        if item > needle:
            r.append(item)
        else:
            l.append(item)

    if l:
        l = quicksort(l)
    if r:
        r = quicksort(r)
    result = l + [needle] + r
    if len(result) > 1:
        print out(result)
    return result


def main():
    _ = input()
    ar = [int(i) for i in raw_input().strip().split()]
    quicksort(ar)


if __name__ == "__main__":
    main()
