def fold_horizontaly(dots, number):
    return [(d[0], number - (d[1] - number)) if d[1] > number else d for d in dots]
    pass

def fold_verticaly(dots, number):
    return [(number - (d[0] - number), d[1]) if d[0] > number else d for d in dots]
    pass

def fold(dots, operations):
    for o in operations:
        if o[0] == 'y':
            dots = fold_horizontaly(dots, o[1])
        else:
            dots = fold_verticaly(dots, o[1])

    draw_dots(dots)

def draw_dots(dots):
    y = {p[1] for p in dots}
    x = {p[0] for p in dots}
    drawing = [['.' for x in range(max(x) + 1)] for y in range(max(y) + 1)]
    for i in dots:
        drawing[i[1]][i[0]] = '#'
    for d in drawing:
        print(''.join(d))

if __name__ == "__main__":
    with open('input.txt') as f:
        lines, _operations = f.read().split("\n\n")
        lines = str(lines).replace('\n', ',')
        lines = list(map(int, lines.split(',')))
        _dots = []
        for i in range(0, len(lines), 2):
            _dots.append(tuple(lines[i:i+2]))
        _operations = _operations.strip().split('\n')

        temp = []
        for i in _operations:
            dimension, number = i.split('=')
            temp.append([dimension[-1:], int(number)])
        _operations = temp

        fold(set(tuple(_dots)), _operations)
        pass




