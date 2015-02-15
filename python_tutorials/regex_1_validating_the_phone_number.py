import re


def get_phone_numbers(input_list):
    input_list.pop(0)
    return input_list


def number_presenter(f):
    def inner(is_valid):
        is_valid = f(is_valid)
        return "YES" if is_valid else "NO"

    return inner


@number_presenter
def number_validation(input_entry):
    match = re.search(r'^[789]\d{9}$', input_entry)
    return True if match else False


if __name__ == '__main__':
    from fileinput import input

    def get_input():
        return [line.strip() for line in input()]

    user_input = get_input()
    numbers_list = get_phone_numbers(user_input)
    # noinspection PyTypeChecker
    print "\n".join(
        [number_validation(numbers_item) for numbers_item in numbers_list])
