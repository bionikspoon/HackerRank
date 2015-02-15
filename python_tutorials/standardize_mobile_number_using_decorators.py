def get_numbers(numbers_list):
    """
    >>> get_numbers(['3', '07895462130', '919875641230', '9195969878'])
    ['07895462130', '919875641230', '9195969878']
    >>> get_numbers(['3', '09191919191', '9100256236', '+919593621456'])
    ['09191919191', '9100256236', '+919593621456']

    :param numbers_list:
    :return:
    """
    _ = numbers_list.pop(0)
    return numbers_list


def standardize_number(phone_number):
    """
    >>> standardize_number('07895462130')
    '+91 78954 62130'
    >>> standardize_number('919875641230')
    '+91 98756 41230'
    >>> standardize_number('9195969878')
    '+91 91959 69878'
    """

    return "+91 %s %s" % (phone_number[-10:-5], phone_number[-5:])


def standardize_numbers_presenter(func):
    """
    >>> sort_numbers(['07895462130', '919875641230', '9195969878'])
    ['+91 78954 62130', '+91 91959 69878', '+91 98756 41230']
    >>> sort_numbers(['09191919191', '9100256236', '+919593621456'])
    ['+91 91002 56236', '+91 91919 19191', '+91 95936 21456']


    :param func:
    :return:
    """

    def wrapper(numbers):
        standardized_numbers = map(standardize_number, numbers)
        return func(standardized_numbers)

    return wrapper


@standardize_numbers_presenter
def sort_numbers(numbers_list):
    """
    >>> sort_numbers(['07895462130', '919875641230', '9195969878'])
    ['07895462130', '9195969878', '919875641230']
    >>> sort_numbers(['5'*10, '1'*10, '9'*10])
    ['1111111111', '5555555555', '9999999999']
    >>> sort_numbers(['+91 78954 62130', '+91 98756 41230', '+91 91959 69878'])
    ['+91 78954 62130', '91 91959 69878', '+91 98756 41230']

    :param numbers_list:
    :return:
    """
    sorted_numbers_list = sorted(numbers_list)
    return sorted_numbers_list


if __name__ == '__main__':
    from fileinput import input

    def get_input():
        return [line.strip() for line in input()]

    user_input = get_input()
    mobile_numbers = get_numbers(user_input)
    print "\n".join(sort_numbers(mobile_numbers))