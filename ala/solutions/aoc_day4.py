from typing import List, Optional

import numpy as np

from ala.solutions.utils import read_numbers_and_tables


class Bingo:
    def __init__(self, numbers: List[int], tables: List[np.ndarray]):
        self.numbers = numbers
        self.tables = tables
        self.size = len(tables[0][0])

    def find_first_bingo(self) -> Optional[int]:
        index, table = self.first_winning_index_and_table()
        unmarked_sum = self.get_unmarked_sum(table, self.numbers[:index])
        return self.numbers[index - 1] * unmarked_sum

    def find_last_bingo(self) -> Optional[int]:
        win_tables = []

        for index in range(len(self.numbers)):
            for table in tables:
                win_table = set(table.flatten())

                if win_table not in win_tables:
                    for row in table:
                        if all(elem in self.numbers[:index] for elem in row):
                            win_tables.append(win_table)

                if win_table not in win_tables:
                    for column in table.T:
                        if all(elem in self.numbers[:index] for elem in column):
                            win_tables.append(win_table)

                if len(win_tables) == len(tables):
                    unmarked_sum = self.get_unmarked_sum(table, self.numbers[:index])
                    return self.numbers[index - 1] * unmarked_sum

    def get_unmarked_sum(self, table, numbers_to_mark):
        mask = ~np.isin(table, numbers_to_mark)
        return np.sum(table * mask)

    def first_winning_index_and_table(self):
        for index in range(len(self.numbers)):
            if index < self.size:
                continue

            for table in tables:
                for row in table:
                    if all(elem in self.numbers[:index] for elem in row):
                        return index, table

                for column in table.T:
                    if all(elem in self.numbers[:index] for elem in column):
                        return index, table


if __name__ == '__main__':
    input_path = '../inputs/aoc_day4.txt'
    numbers, tables = read_numbers_and_tables(input_path)

    bingo = Bingo(numbers, tables)
    print(bingo.find_first_bingo())
    print(bingo.find_last_bingo())
