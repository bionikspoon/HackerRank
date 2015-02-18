def raise_odd_flag(odd_flag):
    if odd_flag:
        raise TypeError
    else:
        return True


def main(password):
    password = password[0]
    odd_flag = not len(password) % 2

    try:
        for c in set(password):
            if password.count(c) % 2:
                odd_flag = raise_odd_flag(odd_flag)
    except TypeError:
        return "NO"

    return "YES" if odd_flag else "NO"


if __name__ == "__main__":
    from fileinput import input

    def get_input():
        return [line for line in input()]

    print main(get_input())
