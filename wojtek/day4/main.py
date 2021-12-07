def calculate_winning_board_score(bingo_numbers, list_of_board_dicts):
    list_of_board_dicts = [[[0] * 10, x] for x in list_of_board_dicts]
    for n in bingo_numbers:
        for hit_list, board in list_of_board_dicts:
            if n in board:
                x, y = board.pop(n)
                hit_list[x] += 1
                hit_list[y+5] += 1
                if hit_list[x] == 5 or hit_list[y+5] == 5:
                    left_numbers = [int(key) for key, values in board.items()]
                    return sum(left_numbers) * int(n)

def calculate_last_winning_board_score(bingo_numbers, list_of_board_dicts):
    list_of_board_dicts = [[[0] * 10, x] for x in list_of_board_dicts]
    place = 1
    for n in bingo_numbers:
        for i, (hit_list, board) in enumerate(list_of_board_dicts):
            if n in board:
                x, y = board.pop(n)
                hit_list[x] += 1
                hit_list[y + 5] += 1
                if hit_list[x] == 5 or hit_list[y + 5] == 5:
                    if place < len(list_of_board_dicts):
                        list_of_board_dicts[i][1].clear()
                        place += 1
                    else:
                        left_numbers = [int(key) for key, values in board.items()]
                        return sum(left_numbers) * int(n)

if __name__ == "__main__":
    with open("input.txt") as f:
        numbers = f.readline().split(",")
        lines = [line.strip() for line in f.readlines() if not line.isspace()]
        boards = [lines[x:x+5] for x in range(0, len(lines), 5)]

        ld = []
        for b in boards:
            d = {}
            for y, lines in enumerate(b):
                for x, n in enumerate(lines.split()):
                    d[n] = [x, y]
            ld.append(d)

        print(calculate_last_winning_board_score(numbers, ld))