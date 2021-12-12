from typing import Tuple, List

from tqdm import tqdm

from ala.solutions.utils import read_connections


class Graph:
    def __init__(self, connections: List[Tuple[str, str]]):
        self.start = Node('start')
        self.end = Node('end')
        self.nodes = [self.start, self.end]

        for start_node_val, end_node_val in connections:
            if start_node_val not in self.nodes:
                start_node = Node(start_node_val)
                self.nodes.append(start_node)
            else:
                start_node = [node for node in self.nodes if node.value == start_node_val][0]

            if end_node_val not in self.nodes:
                end_node = Node(end_node_val)
                self.nodes.append(end_node)
            else:
                end_node = [node for node in self.nodes if node.value == end_node_val][0]

            if end_node not in start_node.neighbours:
                start_node.neighbours.append(end_node)

            if start_node not in end_node.neighbours:
                end_node.neighbours.append(start_node)


class Node:
    def __init__(self, value: str):
        self.value = value
        self.one_visit_possible = value.islower()
        self.two_visit_possible = False
        self.neighbours = []

    def __str__(self):
        return self.value

    def __eq__(self, other):
        return self.value == other

    def __repr__(self):
        return str(self)


class PathFinder:
    def __init__(self, connections: List[Tuple[str, str]]):
        self.graph = Graph(connections)
        self.small_caves = self._get_small_caves(connections)
        self.paths = []

    @staticmethod
    def _get_small_caves(connections):
        small_caves = []
        for start_node_val, end_node_val in connections:
            if start_node_val.islower() and start_node_val not in small_caves:
                small_caves.append(start_node_val)
            if end_node_val.islower() and end_node_val not in small_caves:
                small_caves.append(end_node_val)
        small_caves.remove('start')
        small_caves.remove('end')
        return small_caves

    def find_all_paths(self):
        for small_cave in tqdm(self.small_caves):
            [node for node in self.graph.nodes if node.value == small_cave][0].one_visit_possible = False
            [node for node in self.graph.nodes if node.value == small_cave][0].two_visit_possible = True

            self.find_all_paths_(self.graph.start, [])

            [node for node in self.graph.nodes if node.value == small_cave][0].one_visit_possible = True
            [node for node in self.graph.nodes if node.value == small_cave][0].two_visit_possible = False
        return len(self.paths)

    def find_all_paths_(self, node: Node, actual_path: List[str]):
        if node.one_visit_possible and node.value in actual_path:
            return

        if node.two_visit_possible and actual_path.count(node.value) > 1:
            return

        new_path = actual_path + [node]

        if node == self.graph.end:
            if new_path not in self.paths:
                self.paths.append(new_path)
            return

        for neighbour in node.neighbours:
            self.find_all_paths_(neighbour, new_path)


if __name__ == '__main__':
    input_path = '../inputs/aoc_day12.txt'
    connections = read_connections(input_path)

    pf = PathFinder(connections)
    print(pf.find_all_paths())
