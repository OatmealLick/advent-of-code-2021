import math
from collections import Counter, defaultdict


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    template = lines[0]
    rules = {}
    for line in lines[2:]:
        parts = [part.strip() for part in line.split("->")]
        rules[parts[0]] = parts[1]

    dict_template = defaultdict(lambda: 0)
    i = 1
    while i < len(template):
        rule_key = template[i - 1] + template[i]
        dict_template[rule_key] += 1
        i += 1

    steps = 40
    for step in range(steps):
        new_dict_template = defaultdict(int)
        for pair, count in dict_template.items():
            rule = rules[pair]
            first = pair[0] + rule
            second = rule + pair[1]
            new_dict_template[first] += count
            new_dict_template[second] += count
        dict_template = new_dict_template
        print(f"Template {dict_template}, count {sum(dict_template.values())}")

    occurrences = defaultdict(lambda: 0)
    for pair, count in dict_template.items():
        for letter in pair:
            occurrences[letter] += count
    print(occurrences)
    values = occurrences.values()
    max_value = math.ceil(max(values) / 2)
    min_value = math.ceil(min(values) / 2)
    print(f"Max {max_value}, min: {min_value}")
    print(max_value - min_value)


if __name__ == "__main__":
    main()
