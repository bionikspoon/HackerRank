import re


def get_input():
    return [line.strip() for line in input()]


def get_email_list(input_list):
    _ = input_list.pop(0)
    return input_list


def validate_email(email_string):
    match = re.search(r'^[\w-]+@[a-zA-Z0-9]+\.\w\w?\w?$', email_string)
    return True if match else False


if __name__ == '__main__':
    from fileinput import input

    user_input = get_input()
    email_list = get_email_list(user_input)
    print sorted(filter(validate_email, email_list))
