import os
import sys
from collections import defaultdict
from typing import List, Dict


class Path:
    def __init__(self, path, duplicated_lower):
        self.path = path
        self.duplicated_lower = duplicated_lower

    def __eq__(self, o: object) -> bool:
        return self.path == o.path and self.duplicated_lower == o.duplicated_lower

    def __str__(self) -> str:
        return f"dup: {self.duplicated_lower}, path: {self.path}"

    def __repr__(self) -> str:
        return str(self)

    def __hash__(self) -> int:
        return self.path.__hash__() + 31 * self.duplicated_lower

    def __iter__(self):
        return self.path.__iter__()


def find_paths(connections: Dict[str, List[str]], end: str = 'end'):
    lowers = [k for k in connections.keys() if k.islower()]
    paths = []
    for lower in lowers:
        if lower not in ['start', 'end']:
            paths.append(Path(['start'], lower))
    unfinished_paths = []
    finished_paths = []
    for i in range(len(paths)):
        if paths[i].path[-1] != end:
            unfinished_paths.append(paths[i])
    while unfinished_paths:
        for path in unfinished_paths:
            # print(f"Before remove: {paths}")
            paths.remove(path)
            # print(f"After remove: {paths}")
            for n in connections[path.path[-1]]:
                if can_be_visited(n, path):
                    new_path = Path(path.path.copy() + [n], path.duplicated_lower)
                    paths.append(new_path)
        unfinished_paths = []
        new_paths = []
        for i in range(len(paths)):
            if paths[i].path[-1] != end:
                unfinished_paths.append(paths[i])
            else:
                finished_paths.append(paths[i])


        print(f"Paths len: {len(paths)}")
        # print(f"Paths: {paths}")
        # print(f"Unfinished : {unfinished_paths}")
    duplicated_paths = map(lambda p: p.path, paths)
    not_duplicated_paths = []
    for p in duplicated_paths:
        if p not in not_duplicated_paths:
            not_duplicated_paths.append(p)
    return not_duplicated_paths


def can_be_visited(n: str, path: Path):
    if n in ['start']:
        return False
    if n.isupper():
        return True
    ns = [n_ for n_ in path.path if n_ == n]
    count = len(ns)
    return count < 1 or (count < 2 and n == path.duplicated_lower)


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
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
