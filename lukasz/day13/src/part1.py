from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
Fold = namedtuple('Fold', ['axis', 'value'])


def perform_fold_y(value: int, points: list):
    points_to_throw = [p for p in points if p.y > value]
    for p in points_to_throw:
        points.remove(p)
        corresponding = value * 2 - p.y
        new_p = Point(p.x, corresponding)
        if new_p not in points:
            points.append(new_p)


def perform_fold_x(value: int, points: list):
    points_to_throw = [p for p in points if p.x > value]
    for p in points_to_throw:
        points.remove(p)
        corresponding = value * 2 - p.x
        new_p = Point(corresponding, p.y)
        if new_p not in points:
            points.append(new_p)


def perform_fold(fold, points):
    if fold.axis == 'x':
        perform_fold_x(fold.value, points)
    else:
        perform_fold_y(fold.value, points)


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    points = []
    folds = []
    line = lines.pop(0)
    while line:
        parts = [int(part.strip()) for part in line.split(",")]
        points.append((Point(parts[0], parts[1])))
        line = lines.pop(0)

    for line in lines:
        parts = [part.strip() for part in line[11:].split("=")]
        folds.append(Fold(parts[0], int(parts[1])))

    fold_count = len(folds)
    for i in range(fold_count):
        perform_fold(folds[i], points)

    for y in range(6):
        line = ""
        for x in range(40):
            line += "#" if Point(x, y) in points else "."
        print(line)


if __name__ == "__main__":
    main()
