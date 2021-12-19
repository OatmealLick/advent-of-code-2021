
def check_line_for_corruption(line):
    left_brackets = ('(', '[', '{', '<')
    brackets = {'(': 3, '[': 57, '{': 1197, '<': 25137, ')': 3, ']': 57, '}': 1197, '>': 25137}
    queue = []
    for b in line:
        if b in left_brackets:
            queue.append(brackets[b])
        elif queue.pop() == brackets[b]:
            pass
        else:
            return brackets[b]
    return 0

def autocomplete_line(line):
    left_brackets = ('(', '[', '{', '<')
    brackets = {'(': 1, '[': 2, '{': 3, '<': 4, ')': 1, ']': 2, '}': 3, '>': 4}
    queue = []
    for b in line:
        if b in left_brackets:
            queue.append(brackets[b])
        elif queue.pop() == brackets[b]:
            pass
        else:
            return 0
    score = 0
    for n in range(len(queue)):
        score = (score * 5) + queue.pop()

    return score

def part1(lines):
    score = 0
    for line in lines:
        score += check_line_for_corruption(line)
    print(score)

def part2(lines):
    scores = []
    for line in lines:
        score = autocomplete_line(line)
        if score:
            scores.append(score)

    print(sorted(scores)[len(scores)//2])


if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.read().splitlines()
        part1(lines)
        part2(lines)



