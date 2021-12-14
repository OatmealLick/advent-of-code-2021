from copy import deepcopy
from typing import Dict

from ala.solutions.utils import read_polymer


class PolymerGenerator:
    def __init__(self, polymer: Dict[str, str], rules: Dict[str, str]):
        self.polymer_pairs = polymer
        self.polymer = {}
        self.rules = rules

    def count_difference(self, steps: int) -> int:
        self._update_polymer(steps)
        polymer = self._get_polymer()
        max_occurrences = max(polymer.values())
        min_occurrences = min(polymer.values())
        return (max_occurrences - min_occurrences)/2

    def _get_polymer(self):
        polymer = {}
        for pair in self.polymer_pairs.keys():
            first, second = pair
            occ = self.polymer_pairs[pair]

            if first in polymer:
                polymer[first] += occ
            else:
                polymer[first] = occ

            if second in polymer:
                polymer[second] += occ
            else:
                polymer[second] = occ

        return polymer

    def _update_polymer(self, steps: int):
        for _ in range(steps):
            updated_polymer = deepcopy(self.polymer_pairs)
            for pair in self.polymer_pairs:
                pair_occurrences = self.polymer_pairs[pair]
                inserted_element = self.rules[pair]
                first_new_pair = pair[0] + inserted_element
                second_new_pair = inserted_element + pair[1]

                updated_polymer[pair] -= pair_occurrences

                if first_new_pair in updated_polymer:
                    updated_polymer[first_new_pair] += pair_occurrences
                else:
                    updated_polymer[first_new_pair] = pair_occurrences

                if second_new_pair in updated_polymer:
                    updated_polymer[second_new_pair] += pair_occurrences
                else:
                    updated_polymer[second_new_pair] = pair_occurrences
            self.polymer_pairs = updated_polymer


if __name__ == '__main__':
    input_path = '../inputs/aoc_day14.txt'
    template, rules = read_polymer(input_path)

    pg = PolymerGenerator(template, rules)
    print(pg.count_difference(40))
