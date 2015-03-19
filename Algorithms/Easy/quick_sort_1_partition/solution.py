# coding=utf-8
def partition(ar):
    pre = []
    post = []
    n = ar[0]
    for item in ar[1:]:
        if item > n:
            post.append(item)
        else:
            pre.append(item)
    ar = pre + [n] + post

    return ar


def main():
    m = input()
    ar = [int(i) for i in raw_input().strip().split()]
    ar = partition(ar)
    out = lambda x: ' '.join(map(str, x))
    print out(ar)


if __name__ == "__main__":
    main()
