from typing import List, Optional, Tuple

from ala.solutions.utils import read_str_input


class SyntaxErrorDetector:
    def __init__(self, chunks: List[str]):
        self.chunks = chunks
        self.pairs = {
            '(': ')',
            '[': ']',
            '{': '}',
            '<': '>'
        }
        self.scores = {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137
        }
        self.filling_scores = {
            ')': 1,
            ']': 2,
            '}': 3,
            '>': 4
        }

    def find_syntax_error_score(self):
        score = 0
        for line in self.chunks:
            invalid_chunk, _ = self.find_first_invalid_chunk(line)
            if invalid_chunk:
                score += self.scores[invalid_chunk]
        return score

    def find_missing_chunks_score(self):
        scores = []
        for line in self.chunks:
            line = line.strip()
            invalid_chunk, open_opens = self.find_first_invalid_chunk(line)
            if not invalid_chunk:
                scores.append(self.find_missing_closes_score(open_opens))

        scores.sort()
        return scores[len(scores) // 2]

    def find_first_invalid_chunk(self, line) -> Tuple[Optional[str], List[str]]:
        opens = []
        for chunk in line:
            if chunk in self.pairs.keys():
                opens.append(chunk)
            if chunk in self.pairs.values():
                last_open = opens.pop()
                if self.pairs[last_open] != chunk:
                    return chunk, opens
        return None, opens

    def find_missing_closes_score(self, open_opens):
        score = 0
        open_opens.reverse()
        for open_ in open_opens:
            score *= 5
            score += self.filling_scores[self.pairs[open_]]
        return score


if __name__ == '__main__':
    input_path = '../inputs/aoc_day10.txt'
    chunks = read_str_input(input_path)

    sed = SyntaxErrorDetector(chunks)
    # print(sed.find_syntax_error_score())
    print(sed.find_missing_chunks_score())
