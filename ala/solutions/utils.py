from typing import List


def read_input(path: str) -> List[int]:
    with open(path) as file:
        return [int(line) for line in file.readlines()]