from itertools import combinations


def main(_input):
    n, m = map(int, _input.pop(0).split(" "))
    people = map(lambda x: int(x, 2), _input)
    team_options = [bin(people[a] | people[b]).count('1') for a, b in
                    combinations(xrange(n), 2)]
    max_topics = max(team_options)
    max_teams = team_options.count(max_topics)
    return map(str, (max_topics, max_teams))


if __name__ == "__main__":
    from fileinput import input

    def get_input():
        return [line for line in input()]

    solution = main(get_input())
    print "\n".join(solution)
