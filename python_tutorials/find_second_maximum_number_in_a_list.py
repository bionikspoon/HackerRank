def get_input():
    return [line.strip() for line in input()]


def get_unique_numbers(numbers_list):
    _ = numbers_list.pop(0)
    return set(map(int, numbers_list[0].split(" ")))


def get_second_highest(unique_numbers_list):
    results = sorted(unique_numbers_list, key=None, reverse=True)
    if len(results) == 0:
        return results[0]
    return results[1]


if __name__ == '__main__':
    from fileinput import input

    user_input = get_input()
    unique_numbers = get_unique_numbers(user_input)
    print get_second_highest(unique_numbers)
