from typing import List, Tuple

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


def read_lines_coords(path: str) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    lines_coords = []

    with open(path) as file:
        for line in file.readlines():
            line = line.strip()
            start_point, end_point = line.split('->')

            start_point = tuple([int(coord) for coord in start_point.split(',')])
            end_point = tuple([int(coord) for coord in end_point.split(',')])

            lines_coords.append((start_point, end_point))

    return lines_coords


def read_one_line_int(path: str) -> List[int]:
    with open(path) as file:
        numbers = file.readline()
        numbers = [int(num) for num in numbers.split(',')]
    return numbers


def read_codes(path: str) -> List[Tuple[List[str], List[str]]]:
    with open(path) as file:
        codes = []
        for line in file.readlines():
            entry, output = line.split('|')
            entry, output = entry.split(' '), output.split(' ')
            entry = [e.strip() for e in entry if len(e.strip()) > 0]
            output = [o.strip() for o in output if len(o.strip()) > 0]
            codes.append((entry, output))
        return codes


def read_map(path: str) -> np.ndarray:
    map = []
    with open(path) as file:
        for row in file.readlines():
            map.append([int(number) for number in row.strip()])
    return np.array(map)


def read_connections(path: str) -> List[Tuple[str, str]]:
    connections = []
    with open(path) as file:
        for row in file.readlines():
            start_node, end_node = row.strip().split('-')
            connections.append((start_node, end_node))

    return connections


def read_dots_and_folds(path: str) -> (List[Tuple[int, int]], List[Tuple[str, int]]):
    coords = []
    folds = []
    with open(path) as file:
        for row in file.readlines():
            if len(row.strip()) == 0:
                continue
            if 'fold' not in row:
                x_, y_ = row.strip().split(',')
                coords.append((int(x_), int(y_)))
            else:
                if 'y' in row:
                    y = int(row.strip().split('=')[1])
                    folds.append(('y', y))
                if 'x' in row:
                    x = int(row.strip().split('=')[1])
                    folds.append(('x', x))
    return coords, folds


def read_polymer(path: str):
    with open(path) as file:
        rules = {}

        polymer_template = file.readline().strip()
        polymer = {}
        for pos in range(len(polymer_template)):
            pair = polymer_template[pos:pos + 2]
            if len(pair) == 2:
                if pair in polymer:
                    polymer[pair] += 1
                else:
                    polymer[pair] = 1

        for row in file.readlines():
            if '->' in row:
                row = row.strip()
                pair, insert = row.split('->')
                rules[pair.strip()] = insert.strip()

    return polymer, rules
