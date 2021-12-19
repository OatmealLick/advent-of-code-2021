import os
import sys

autocompletion_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

matching_closing_chars = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


def opening():
    return ['(', '[', '{', '<']


def closing():
    return [')', ']', '}', '>']


def match_them_okaaaaaaaaaaaay(char): # https://www.youtube.com/watch?v=1FhwCBkhoRg&t=21s
    return matching_closing_chars[char]


def autocompletion_score(char):
    return autocompletion_points[char]


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    scores = []
    for line in lines:
        has_error, opened = has_errors(line)
        if not has_error:
            score = compute_score(opened)
            scores.append(score)
    scores.sort()
    print(f"Scores {scores}")
    print(f"Middle {scores[len(scores) // 2]}")


def compute_score(opened):
    opened.reverse()
    score = 0
    for char in opened:
        closed_char = match_them_okaaaaaaaaaaaay(char)
        score *= 5
        score += autocompletion_score(closed_char)
    return score


def has_errors(line):
    opened = []
    for char in line:
        if char in opening():
            opened.append(char)
        else:
            last_opened = opened.pop()
            if char != match_them_okaaaaaaaaaaaay(last_opened):
                print(f"For line {line} got error with {char}")
                return True, opened
    return False, opened


if __name__ == "__main__":
    main()
