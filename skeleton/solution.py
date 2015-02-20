def solve_me_second(a, b):
    return a + b


def main():
    n = int(raw_input())
    for _ in range(n):
        a, b = map(int, input().split())
        res = solve_me_second(a, b)
        print res


if __name__ == "__main__":
    main()
