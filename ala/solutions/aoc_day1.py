from typing import List

from ala.solutions.utils import read_int_input


class DepthIncreasesMeter:
    def __init__(self, measurements: List[int]):
        self.measurements = measurements

    def count_increased_measurements(self):
        counter = 0
        for index in range(1, len(self.measurements)):
            counter += self.measurements[index] > self.measurements[index - 1]
        return counter

    def count_increased_measurements_triplets(self):
        counter = 0
        for index in range(len(self.measurements) - 3):
            first_triplet = [self.measurements[index_] for index_ in range(index, index + 3)]
            second_triplet = [self.measurements[index_] for index_ in range(index + 1, index + 4)]
            counter += sum(second_triplet) > sum(first_triplet)
        return counter


if __name__ == '__main__':
    input_path = '../inputs/aoc_day1.txt'
    measurements = read_int_input(input_path)
    depth_increases_meter = DepthIncreasesMeter(measurements)

    print(depth_increases_meter.count_increased_measurements())
    print(depth_increases_meter.count_increased_measurements_triplets())
