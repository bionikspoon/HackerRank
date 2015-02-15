def get_input():
    return [line.strip() for line in input()]


def search_string(needle, haystack):
    """
    >>>search_string("CDC", "ABCDCDC")
    2

    :rtype : int
    :param needle:
    :param haystack:
    :return:
    """
    count = 0
    for i in xrange(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            count += 1
    return count


if __name__ == '__main__':
    from fileinput import input

    haystack, needle = get_input()

    print search_string(needle, haystack)