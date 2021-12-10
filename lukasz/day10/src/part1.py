import os
import sys

error_codes = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

def opening():
    return ['(', '[', '{', '<']


def closing():
    return [')', ']', '}', '>']


def matching_closing(char):
    return closing()[opening().index(char)]


def error_code(char):
    return error_codes[char]

def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(filename, "r") as f:
        # to sie nazywa input
        lines = [line.strip() for line in f.readlines()]

    error = 0
    for line in lines:
        opened = []
        for char in line:
            if char in opening():
                opened.append(char)
            else:
                last_opened = opened.pop()
                if char != matching_closing(last_opened):
                    error += error_code(char)
                    print(f"For line {line} got error with {char}")
                    break
    print(f"Error {error}")



if __name__ == "__main__":
    main()
