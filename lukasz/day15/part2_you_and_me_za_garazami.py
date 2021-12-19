import heapq
import sys
from collections import namedtuple, defaultdict

Pos = namedtuple('Pos', ['x', 'y'])


def a_star(cave, start):
    width = len(cave[0]) * 5
    height = len(cave) * 5
    end = Pos(width - 1, height - 1)
    open_set = []
    heapq.heappush(open_set, (heuristic(start, end), start))
    previous_nodes = {}
    g_scores = defaultdict(lambda: sys.maxsize)
    g_scores[start] = 0
    steps = 0

    while open_set:
        steps += 1
        node = heapq.heappop(open_set)[1]
        if node == end:
            print(f"Steps: {steps}")
            return recreate_path(previous_nodes, node, cave)
        for n in neighbours(node, height, width):
            possible_g_score = g_scores[node] + get_cost(n, cave)
            if possible_g_score < g_scores[n]:
                previous_nodes[n] = node
                g_scores[n] = possible_g_score
                f_score = possible_g_score + heuristic(n, end)
                if n not in open_set:
                    heapq.heappush(open_set, (f_score, n))


def heuristic(pos, end):
    return end.x - pos.x + end.y - pos.y


def recreate_path(previous_nodes, node, cave):
    risk = 0
    while node != Pos(0, 0):
        risk += get_cost(node, cave)
        node = previous_nodes[node]
    return risk


def next_node(open_set, f_scores):
    filtered = [p for p in f_scores.items() if p[0] in open_set]
    return min(filtered, key=lambda p: p[1])[0]


def neighbours(pos: Pos, height: int, width: int):
    poses = [Pos(pos.x, pos.y + 1),
             Pos(pos.x, pos.y - 1),
             Pos(pos.x + 1, pos.y),
             Pos(pos.x - 1, pos.y)
             ]
    return [pos for pos in poses if is_within_bounds(pos, height, width)]


def is_within_bounds(pos: Pos, height: int, width: int):
    return 0 <= pos.x < width and 0 <= pos.y < height


def get_cost(pos, cave):
    height = len(cave)
    width = len(cave[0])
    if is_within_bounds(pos, height, width):
        return cave[pos.y][pos.x]
    else:
        y_cells = pos.y // height
        y_offset = pos.y % height
        x_cells = pos.x // width
        x_offset = pos.x % width
        original_cost = cave[y_offset][x_offset]
        cost = original_cost + y_cells + x_cells
        return cost if cost < 10 else cost - 9


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(filename, "r") as f:
        cave = [[int(num) for num in line] for line in f.read().splitlines()]

    risk = a_star(cave, Pos(0, 0))
    print(risk)


if __name__ == "__main__":
    main()
