from collections import defaultdict
import math

def polymerization(rules, polymer):

    pairs = defaultdict(int)
    for i in range(len(polymer) - 1):
        pairs[polymer[i:2 + i]] += 1

    for i in range(40):
        new_pairs = defaultdict(int)
        for key, value in pairs.items():
            new_pairs[key[0] + rules[key]] += value
            new_pairs[rules[key] + key[1]] += value

        pairs = new_pairs

    letter_count = defaultdict(int)
    for key, value in pairs.items():
        letter_count[key[0]] += value
        letter_count[key[1]] += value
    print(math.ceil(max(letter_count.values()) / 2) - math.ceil(min(letter_count.values()) / 2))

if __name__ == "__main__":
    with open('input.txt') as f:
        _polymer, _rules = f.read().strip().split("\n\n")
        _rules = [r.split(" -> ") for r in _rules.split("\n")]
        _rules = {key: value for key, value in _rules}

        polymerization(_rules, _polymer)

        pass
