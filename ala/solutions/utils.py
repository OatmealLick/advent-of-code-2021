from typing import List


def read_int_input(path: str) -> List[int]:
    with open(path) as file:
        return [int(line) for line in file.readlines()]


def read_str_input(path: str) -> List[str]:
    with open(path) as file:
        return [line for line in file.readlines()]
