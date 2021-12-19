def most_common_value(lines):
    values = [0 for t in lines[0]]  # some better way ?
    for line in lines:
        for i, n in enumerate(line):
            values[i] += int(n)
    values = [1 if int(n / (len(lines) / 2)) >= 1 else 0 for n in values]
    return values

def calculate_life_support_rating(inputLines):
    i = 0
    O2_rating, CO2_rating = inputLines, inputLines
    while len(O2_rating) > 1:
        mcvalues = most_common_value(O2_rating)
        O2_rating = [line for line in O2_rating if int(line[i]) == mcvalues[i]]
        i += 1
    i = 0
    while len(CO2_rating) > 1:
        mcvalues = most_common_value(CO2_rating)
        CO2_rating = [line for line in CO2_rating if int(line[i]) != mcvalues[i]]
        i += 1

    return int(O2_rating.pop(), 2) * int(CO2_rating.pop(), 2)


if __name__ == '__main__':
    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
        print(calculate_life_support_rating(lines))
