from typing import Tuple, List

import numpy as np

from ala.solutions.utils import read_dots_and_folds


class DotsCalculator:
    def __init__(self, coordinates: List[Tuple[int, int]], folds: List[Tuple[str, int]]):
        self.coordinates = coordinates
        self.folds = folds

    def calc_all_folds(self):
        for fold in folds:
            self.fold_paper(fold)

        max_x, max_y = 0, 0
        for coord in self.coordinates:
            x, y = coord
            max_x = max(x, max_x)
            max_y = max(y, max_y)

        paper = np.zeros((max_x + 1, max_y + 1))

        for coord in self.coordinates:
            paper[coord[0], coord[1]] = 1

        paper = np.fliplr(paper)
        paper = np.rot90(paper)
        return paper

    def calc_first_fold(self):
        fold = self.folds[0]
        _, result = self.fold_paper(fold)
        return result

    def fold_paper(self, fold):
        if fold[0] == 'x':
            dots, result = self.calc_dots_x_fold(fold[1])
        else:
            dots, result = self.calc_dots_y_fold(fold[1])

        return dots, result

    def calc_dots_y_fold(self, fold_y: int):
        coordinates_y_fold = []

        for coord in self.coordinates:
            x_, y_ = coord
            if y_ == fold_y:
                continue

            if y_ > fold_y:
                dist = y_ - fold_y
                y_ = y_ - 2 * dist

            coordinates_y_fold.append((x_, y_))

        self.coordinates = coordinates_y_fold

        return set(coordinates_y_fold), len(set(coordinates_y_fold))

    def calc_dots_x_fold(self, fold_x: int):
        coordinates_x_fold = []

        for coord in self.coordinates:
            x_, y_ = coord
            if x_ == fold_x:
                continue

            if x_ > fold_x:
                dist = x_ - fold_x
                x_ = x_ - 2 * dist

            coordinates_x_fold.append((x_, y_))

        self.coordinates = coordinates_x_fold

        return set(coordinates_x_fold), len(set(coordinates_x_fold))


if __name__ == '__main__':
    input_path = '../inputs/aoc_day13.txt'
    coordinates, folds = read_dots_and_folds(input_path)

    dc = DotsCalculator(coordinates, folds)
    print(dc.calc_first_fold())
    print(dc.calc_all_folds())
