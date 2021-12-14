from collections import Counter


def main():
    # filename = "input.txt"
    filename = "input-sample.txt"
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    template = lines[0]
    rules = {}
    for line in lines[2:]:
        parts = [part.strip() for part in line.split("->")]
        rules[parts[0]] = parts[1]

    i = 1
    new_template = template[0:1]
    steps = 40
    for step in range(steps):
        while i < len(template):
            rule_key = template[i - 1] + template[i]
            rule = rules[rule_key]
            new_template += rule + template[i]
            i += 1
        i = 1
        cache[template] = new_template
        template = new_template
        new_template = template[0:1]
        # print(f"Template {template}")
        print(f"Steps {step}")
    occurrences = Counter(template)
    values = occurrences.values()
    max_value = max(values)
    min_value = min(values)
    print(f"Max {max_value}, min: {min_value}")
    print(max_value - min_value)


if __name__ == "__main__":
    main()
