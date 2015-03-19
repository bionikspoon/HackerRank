# coding=utf-8
out = lambda x: ' '.join(map(str, x))


def quicksort(haystack, j=None):
    j = len(haystack)-1 if j == None else j
    pivot = haystack[j]
    i = 0
    for j, v in enumerate(haystack):
        if v <= pivot:
            temp = haystack[i]
            haystack[i] = v
            haystack[j] = temp
            i += 1
    quicksort(haystack, j-1)
    return haystack


def main():
    _ = input()
    ar = [int(i) for i in raw_input().strip().split()]
    result = quicksort(ar)
    print out(result)


if __name__ == "__main__":
    main()
