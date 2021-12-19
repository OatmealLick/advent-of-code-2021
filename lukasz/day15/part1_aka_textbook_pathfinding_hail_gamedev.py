import heapq
import sys
from collections import namedtuple, defaultdict

Pos = namedtuple('Pos', ['x', 'y'])


def dijkstra(cave, start):
    stack = []
    width = len(cave[0])
    height = len(cave)
    for row in range(height):
        for col in range(width):
            stack.append(Pos(row, col))
    end = Pos(width - 1, height - 1)
    distances = defaultdict(lambda: sys.maxsize)
    distances[start] = 0
    previous_nodes = {}
    while stack:
        current = minimal_distance(distances, stack)
        stack.remove(current)
        if current == end:
            break

        ns = [n for n in neighbours(current, height, width) if n in stack]
        for n in ns:
            possible_better = distances[current] + cave[n.y][n.x]
            if possible_better < distances[n]:
                distances[n] = possible_better
                previous_nodes[n] = current
    risk = 0
    pos = end
    while pos != start:
        risk += cave[pos.y][pos.x]
        pos = previous_nodes[pos]
    return risk


def minimal_distance(distances, q):
    filtered = [p for p in distances.items() if p[0] in q]
    return min(filtered, key=lambda p: p[1])[0]


def a_star(cave, start):
    width = len(cave[0])
    height = len(cave)
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
            possible_g_score = g_scores[node] + cave[n.y][n.x]
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
        risk += cave[node.y][node.x]
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


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(filename, "r") as f:
        cave = [[int(num) for num in line] for line in f.read().splitlines()]

    # risk = dijkstra(cave, Pos(0, 0))
    risk = a_star(cave, Pos(0, 0))
    print(risk)


if __name__ == "__main__":
    main()
