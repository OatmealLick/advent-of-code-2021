import os
import sys
from collections import defaultdict
from typing import List, Dict


def find_paths(connections: Dict[str, List[str]], end: str = 'end'):
    paths = [['start']]
    unfinished_paths = [path for path in paths if path[-1] != end]
    while unfinished_paths:
        for path in unfinished_paths:
            paths.remove(path)
            for n in connections[path[-1]]:
                if can_be_visited(n, path):
                    paths.append(path + [n])
        unfinished_paths = [path for path in paths if path[-1] != end]
        print(f"Paths len: {len(paths)}")
        # print(f"Paths: {paths}")
        # print(f"Unfinished : {unfinished_paths}")
    return paths


def can_be_visited(n: str, path: List[str]):
    return n.isupper() or n not in path


def main():
    # filename = "input.txt"
    filename = "input-sample.txt"
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    connections = defaultdict(lambda: [])
    for line in lines:
        parts = [part.strip() for part in line.split("-")]
        connections[parts[0]] += [parts[1]]
        connections[parts[1]] += [parts[0]]
        # todo check if duplicates
    print(connections)
    paths = find_paths(connections)
    print(f"Count: {len(paths)}")


if __name__ == "__main__":
    main()
