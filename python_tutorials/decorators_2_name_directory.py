def create_table(data_list):
    _ = data_list.pop(0)
    keys = ["f_name", "l_name", "age", "gender"]
    return [{k: v for k, v in zip(keys, entry.split(" "))} for entry in
            data_list]


def item_presenter(f):
    def wrapper(*args):
        items_list = f(*args)
        return [proper_name(items) for items in items_list]

    def proper_name(fields):
        title = {"M": "Mr.", "F": "Ms."}
        return "%s %s %s" % (
            title.get(fields.get("gender")), fields.get("f_name"),
            fields.get("l_name"))

    return wrapper


@item_presenter
def sort_items_by(items, attribute):
    return sorted(items, key=lambda x: x[attribute])


if __name__ == '__main__':
    from fileinput import input

    def get_input():
        return [line.strip() for line in input()]

    user_input = get_input()
    user_table = create_table(user_input)
    user_table_sorted = sort_items_by(user_table, "age")
    print "\n".join(user_table_sorted)
