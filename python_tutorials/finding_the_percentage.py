def create_table(data):
    _ = data.pop(0)
    lookup = data.pop()
    table = {}
    for entry in data:
        entry = entry.split(" ")
        table[entry[0]] = (float(entry[1]), float(entry[2]), float(entry[3]))

    return table, lookup


def get_student_average(lookup, table):
    student_grades = table[lookup]
    return sum(student_grades) / float(len(student_grades))


if __name__ == '__main__':
    import fileinput

    user_input = [line.strip() for line in fileinput.input()]
    grade_table, student = create_table(user_input)
    student_average = get_student_average(student, grade_table)
    print "%.2f" % student_average