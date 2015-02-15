def get_stdin():
    raw_input()
    list_1 = raw_input().split()
    raw_input()
    list_2 = raw_input().split()
    return list_1, list_2


if __name__ == '__main__':
    set_m, set_n = get_stdin()
    set_m = set(set_m)
    set_n = set(set_n)
    result = []
    result.extend(set_m.difference(set_n))
    result.extend(set_n.difference(set_m))
    print "\n".join(sorted(result, key=lambda x: int(x)))