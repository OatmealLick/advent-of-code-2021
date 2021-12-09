from typing import List, Tuple

from ala.solutions.utils import read_codes


class CodeDecoder:
    def __init__(self, codes_list: List[Tuple[List[str], List[str]]]):
        self.codes_list = codes_list

    def count_simple_digits_in_output(self):
        simple_digits_in_output = 0
        for code in self.codes_list:
            _, output = code
            for digit in output:
                if len(digit) in [2, 3, 4, 7]:
                    simple_digits_in_output += 1
        return simple_digits_in_output


if __name__ == '__main__':
    input_path = '../inputs/aoc_day8.txt'
    codes_list = read_codes(input_path)

    cd = CodeDecoder(codes_list)
    print(cd.count_simple_digits_in_output())
