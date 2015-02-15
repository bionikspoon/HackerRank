def get_stdin():
    n = raw_input()
    results = [n]
    for i in range(int(n) * 2):
        results.append(raw_input())
    return results


def get_grades(user_input):
    int(user_input.pop(0))
    results = []
    while user_input:
        results.append((user_input.pop(0), float(user_input.pop(0))))
    return results


def get_second_lowest_grade(grade_list):
    ordered_by_grades = sorted(grade_list, key=lambda x: x[1])
    lowest_grade = ordered_by_grades[0][1]
    for student in ordered_by_grades:
        if student[1] > lowest_grade:
            return student[1]


def get_students_with_grade(grade_list, grade_target):
    return [student[0] for student in grade_list if student[1] == grade_target]


if __name__ == '__main__':
    # input_list = get_stdin()
    input_list = """5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39""".split("\n")
    grades = get_grades(input_list)
    second_lowest_grade = get_second_lowest_grade(grades)
    target_students = get_students_with_grade(grades, second_lowest_grade)
    print "\n".join(sorted(target_students))