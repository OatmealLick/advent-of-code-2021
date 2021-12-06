from collections import Counter
from copy import copy
from typing import List

from tqdm import tqdm

from ala.solutions.utils import read_one_line_int


class LanternfishCounter:
    def __init__(self, lanternfish: List[int]):
        self.lanternfish = lanternfish

    def count_lanternfish_in_day_faster(self, day_number: int):
        actual_lanternfish = Counter(self.lanternfish)
        next_lanternfish = copy(actual_lanternfish)

        for _ in tqdm(range(day_number)):
            for lf, lf_num in actual_lanternfish.items():
                if lf == 0:
                    next_lanternfish[6] += lf_num
                    next_lanternfish[8] += lf_num
                    next_lanternfish[0] -= lf_num
                else:
                    next_lanternfish[lf] -= lf_num
                    next_lanternfish[lf - 1] += lf_num

            actual_lanternfish = copy(next_lanternfish)

        return sum([lf_num for lf_num in actual_lanternfish.values()])

    def count_lanternfish_in_day(self, day_number: int):
        actual_lanternfish = self.lanternfish
        next_lanternfish = []

        for _ in range(day_number):
            for lf in actual_lanternfish:
                if lf > 0:
                    next_lanternfish.append(lf - 1)
                else:
                    next_lanternfish = next_lanternfish + [6, 8]
            actual_lanternfish = next_lanternfish
            next_lanternfish = []

        return len(actual_lanternfish)


if __name__ == '__main__':
    input_path = '../inputs/aoc_day6.txt'
    lanternfish = read_one_line_int(input_path)

    lc = LanternfishCounter(lanternfish)
    print(lc.count_lanternfish_in_day_faster(256))
