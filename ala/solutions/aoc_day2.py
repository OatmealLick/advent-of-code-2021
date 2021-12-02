from typing import List

from ala.solutions.utils import read_str_input


class PositionFinder:
    def __init__(self, instructions: List[str]):
        self.instructions = instructions

    def find_actual_position(self):
        horizontal_position = 0
        depth = 0

        for instruction in self.instructions:
            type_, value_ = instruction.split(' ')
            value_ = int(value_)
            if 'forward' in type_:
                horizontal_position += value_
            elif 'up' in type_:
                depth -= value_
            else:
                depth += value_

        return horizontal_position * depth

    def find_actual_position_manual_version(self):
        horizontal_position = 0
        depth = 0

        aim_depth = 0

        for instruction in self.instructions:
            type_, value_ = instruction.split(' ')
            value_ = int(value_)
            if 'forward' in type_:
                horizontal_position += value_
                depth += aim_depth * value_
            elif 'up' in type_:
                aim_depth -= value_
            else:
                aim_depth += value_

        return horizontal_position * depth


if __name__ == '__main__':
    input_path = '../inputs/aoc_day2.txt'
    instructions = read_str_input(input_path)

    position_finder = PositionFinder(instructions)
    print(position_finder.find_actual_position())
    print(position_finder.find_actual_position_manual_version())
