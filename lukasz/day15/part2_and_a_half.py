import heapq
import sys
from collections import namedtuple, defaultdict

Pos = namedtuple('Pos', ['x', 'y'])


class Solution:
    def __init__(self, cave):
        self.input_width = len(cave[0])
        self.input_height = len(cave)
        self.width = self.input_width * 5
        self.height = self.input_height * 5
        self.cave = cave

    def a_star(self, start):
        end = Pos(self.width - 1, self.height - 1)
        open_set = []
        heapq.heappush(open_set, (self.heuristic(start, end), start))
        previous_nodes = {}
        g_scores = defaultdict(lambda: sys.maxsize)
        g_scores[start] = 0
        steps = 0

        while open_set:
            steps += 1
            node = heapq.heappop(open_set)[1]
            if node == end:
                print(f"Steps: {steps}")
                return self.recreate_path(previous_nodes, node)
            for n in self.neighbours(node):
                possible_g_score = g_scores[node] + self.get_cost(n)
                if possible_g_score < g_scores[n]:
                    previous_nodes[n] = node
                    g_scores[n] = possible_g_score
                    f_score = possible_g_score + self.heuristic(n, end)
                    if n not in open_set:
                        heapq.heappush(open_set, (f_score, n))

    def heuristic(self, pos, end):
        return end.x - pos.x + end.y - pos.y

    def recreate_path(self, previous_nodes, node):
        risk = 0
        while node != Pos(0, 0):
            risk += self.get_cost(node)
            node = previous_nodes[node]
        return risk

    def next_node(self, open_set, f_scores):
        filtered = [p for p in f_scores.items() if p[0] in open_set]
        return min(filtered, key=lambda p: p[1])[0]

    def neighbours(self, pos: Pos):
        poses = [Pos(pos.x, pos.y + 1),
                 Pos(pos.x, pos.y - 1),
                 Pos(pos.x + 1, pos.y),
                 Pos(pos.x - 1, pos.y)
                 ]
        return [pos for pos in poses if self.is_within_bounds(pos)]

    def is_within_bounds(self, pos: Pos):
        return 0 <= pos.x < self.width and 0 <= pos.y < self.height

    def is_within_input_bounds(self, pos: Pos):
        return 0 <= pos.x < self.input_width and 0 <= pos.y < self.input_height

    def get_cost(self, pos):
        if self.is_within_input_bounds(pos):
            return self.cave[pos.y][pos.x]
        else:
            y_cells = pos.y // self.input_height
            y_offset = pos.y % self.input_height
            x_cells = pos.x // self.input_width
            x_offset = pos.x % self.input_width
            original_cost = self.cave[y_offset][x_offset]
            cost = original_cost + y_cells + x_cells
            return cost if cost < 10 else cost - 9


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(filename, "r") as f:
        cave = [[int(num) for num in line] for line in f.read().splitlines()]

    risk = Solution(cave).a_star(Pos(0, 0))
    print(risk)


if __name__ == "__main__":
    main()
