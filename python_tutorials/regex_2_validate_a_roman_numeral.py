legal_characters = {"I": {"value": 1, "type": "simple"},
                    "IV": {"value": 4, "type": "compound"},
                    "V": {"value": 5, "type": "simple"},
                    "IX": {"value": 9, "type": "compound"},
                    "X": {"value": 10, "type": "simple"},
                    "XL": {"value": 40, "type": "compound"},
                    "L": {"value": 50, "type": "simple"},
                    "XC": {"value": 90, "type": "compound"},
                    "C": {"value": 100, "type": "simple"},
                    "CD": {"value": 400, "type": "compound"},
                    "D": {"value": 500, "type": "simple"},
                    "CM": {"value": 900, "type": "compound"},
                    "M": {"value": 1000, "type": "simple"}, }


class RomanNumeralError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


def split_roman_numeral(numeral_input):
    """
    Iterate through input, delimit into list.

    >>> split_roman_numeral('CDXXI')
    ['CD', 'X', 'X', 'I']
    >>> split_roman_numeral('DL')
    ['D', 'L']
    >>> split_roman_numeral('XXIV')
    ['X', 'X', 'IV']
    >>> split_roman_numeral('CMCDXCXLIXIVI')
    ['CM', 'CD', 'XC', 'XL', 'IX', 'IV', 'I']
    >>> split_roman_numeral('IIVXLDCM')
    ['I', 'IV', 'XL', 'D', 'CM']
    >>> split_roman_numeral('XLIIII')
    ['XL', 'I', 'I', 'I', 'I']
    >>> split_roman_numeral('XLIV')
    ['XL', 'IV']
    >>> split_roman_numeral('VIIII')
    ['V', 'I', 'I', 'I', 'I']
    >>> split_roman_numeral('MANU')
    Traceback (most recent call last):
    RomanNumeralError: Illegal Character
    >>> split_roman_numeral('I')
    ['I']
    >>> split_roman_numeral('D')
    ['D']
    >>> split_roman_numeral('VV')
    ['V', 'V']
    >>> split_roman_numeral('DD')
    ['D', 'D']
    >>> split_roman_numeral('MMMCMXCIX')
    ['M', 'M', 'M', 'CM', 'XC', 'IX']

    :param numeral_input:
    :return:
    """
    i = 0
    result = []
    while i < len(numeral_input):

        if legal_characters.get(numeral_input[i:i + 2]):
            legal_max = numeral_input[i:i + 2]
        elif legal_characters.get(numeral_input[i]):
            legal_max = numeral_input[i]
        else:
            raise RomanNumeralError("Illegal Character")
        result.append(legal_max)
        i += 2 if legal_characters[legal_max]["type"] == "compound" else 1

    return result


def validate_order(numeral_input):
    """
    Each digit is == or > next digit, or error.

    >>> validate_order(['CD', 'X', 'X', 'I'])
    True
    >>> validate_order(['D', 'L'])
    True
    >>> validate_order(['X', 'X', 'IV'])
    True
    >>> validate_order(['CM', 'CD', 'XC', 'XL', 'IX', 'IV', 'I'])
    True
    >>> validate_order(['XL', 'I', 'I', 'I', 'I'])
    True
    >>> validate_order( ['V', 'I', 'I', 'I', 'I'])
    True
    >>> validate_order( ['I'])
    True
    >>> validate_order( ['M'])
    True
    >>> validate_order( ['V', 'V'])
    True
    >>> validate_order( ['D', 'D'])
    True
    >>> validate_order( ['M', 'M', 'M', 'CM', 'XC', 'IX'])
    True
    >>> validate_order(['IV', 'XL'])
    Traceback (most recent call last):
    RomanNumeralError: Invalid Order
    >>> validate_order(['I', 'IV', 'XL', 'D', 'CM'])
    Traceback (most recent call last):
    RomanNumeralError: Invalid Order

    :param numeral_input:
    :return:
    """
    values = map(lambda x: legal_characters.get(x)["value"], numeral_input)
    for i in xrange(len(values) - 1):
        if values[i] < values[i + 1]:
            raise RomanNumeralError("Invalid Order")

    return True


def validate_repitition(numeral_input):
    """
    >>> validate_repitition(['CD', 'X', 'X', 'I'])
    True
    >>> validate_repitition(['CM', 'CD', 'XC', 'XL', 'IX', 'IV', 'I'])
    True
    >>> validate_repitition(['I'])
    True
    >>> validate_repitition( ['V', 'V'])
    Traceback (most recent call last):
    RomanNumeralError: Repitition Error
    >>> validate_repitition( ['D', 'D'])
    Traceback (most recent call last):
    RomanNumeralError: Repitition Error
    >>> validate_repitition(['M', 'M', 'M', 'CM', 'XC', 'IX'])
    True
    >>> validate_repitition(['XL', 'I', 'I', 'I', 'I'])
    Traceback (most recent call last):
    RomanNumeralError: Repitition Error
    >>> validate_repitition( ['V', 'I', 'I', 'I', 'I'])
    Traceback (most recent call last):
    RomanNumeralError: Repitition Error
    >>> validate_repitition(['CD', 'X', 'IX', 'IX'])
    Traceback (most recent call last):
    RomanNumeralError: Repitition Error

    :param numeral_input:
    :return:
    """
    if len(numeral_input) >= 4:
        for i in xrange(len(numeral_input) - 3):
            if legal_characters.get(numeral_input[i])["type"] == "simple" and \
                            numeral_input[i] == numeral_input[i + 3]:
                raise RomanNumeralError("Repitition Error")

    if len(numeral_input) >= 2:
        for i in xrange(len(numeral_input) - 1):
            if legal_characters.get(numeral_input[i])["type"] == "compound" and \
                            numeral_input[i] == numeral_input[i + 1]:
                raise RomanNumeralError("Repitition Error")
            if numeral_input[i] in ['V', 'L', 'D'] and numeral_input[i] == \
                    numeral_input[i + 1]:
                raise RomanNumeralError("Repitition Error")

    return True


if __name__ == '__main__':
    from fileinput import input

    def get_input():
        return [line.strip() for line in input()][0]

    try:
        user_input = get_input()
        # delimit the input, check all characters are valid
        # CDXXI => ['CD', 'X', 'X', 'I']
        roman_numeral_list = split_roman_numeral(user_input)

        # check x[i] >= x[i+1], check characters are in proper order
        in_order = validate_order(roman_numeral_list)

        # check x[i] != x[i+3], check no character is 3 in a row.
        correct_structure = validate_repitition(roman_numeral_list)

    except RomanNumeralError as e:
        print False

    else:
        print True
