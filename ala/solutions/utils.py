from typing import List

import numpy as np


def read_int_input(path: str) -> List[int]:
    with open(path) as file:
        return [int(line) for line in file.readlines()]


def read_str_input(path: str) -> List[str]:
    with open(path) as file:
        return [line for line in file.readlines()]


def read_numbers_and_tables(path: str) -> (List[int], List[np.ndarray]):
    tables = []

    with open(path) as file:
        numbers = [int(num) for num in file.readline().replace('\n', '').split(',')]
        rows = [line for line in file.readlines()]

        table = []
        for row in rows:
            if len(row) == 1 and '\n' in row and table:
                table = np.array(table)
                tables.append(table)
                table = []
            elif len(row) == 1 and '\n' in row:
                continue
            else:
                row = [int(num) for num in row.replace('\n', '').split(' ') if ' ' not in num and num]
                table.append(row)

        return numbers, tables
