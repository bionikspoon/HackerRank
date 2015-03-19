def beast_key(r):
    threes, fives = 0, 0

    d, r = divmod(r, 15)
    fives += d * 15

    optimize = {14: (5, 9), 13: (10, 3), 12: (0, 12), 11: (5, 6), 10: (10, 0),
                9: (0, 9), 8: (5, 3), 7: (10, -3), 6: (0, 6), 5: (5, 0),
                4: (10, -6), 3: (0, 3), 2: (5, -3), 1: (10, -9), 0: (0, 0)}
    optimize = optimize.get(r) if optimize.get(r) else (-1, -1)

    threes += optimize[0]
    fives += optimize[1]

    return -1 if threes < 0 or fives < 0 else int('5' * fives + '3' * threes)


def main(data):
    _ = data.pop(0)
    keys = [beast_key(int(case)) for case in data]
    return keys


if __name__ == "__main__":
    from fileinput import input

    print "\n".join(map(str, main([item.strip() for item in input()])))