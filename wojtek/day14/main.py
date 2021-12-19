def polymerization(rules, polymer):

    for n in range(40):
        new_polymer_list = []
        for i, c in enumerate(polymer):
            slice = polymer[i:2 + i]
            if slice in _rules.keys():
                new_polymer_list.append(slice[0] + rules[slice])
            else:
                new_polymer_list.append(c)

        polymer = "".join(new_polymer_list)

    polymer_set = set(polymer)
    polymer_count = {}
    for p in polymer_set:
        polymer_count[p] = polymer.count(p)
    print(max(polymer_count.values()) - min(polymer_count.values()))


if __name__ == "__main__":
    with open('small.txt') as f:
        _polymer, _rules = f.read().strip().split("\n\n")
        _rules = [r.split(" -> ") for r in _rules.split("\n")]
        _rules = {key: value for key, value in _rules}

        polymerization(_rules, _polymer)

        pass
