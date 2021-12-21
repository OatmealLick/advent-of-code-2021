from collections import defaultdict, namedtuple


def position_after_roll(start, roll):
    return ((start + roll - 1) % 10) + 1


def next_turn(turn):
    return (turn + 1) % 6


def play_game(p1, p2, p1score, p2score, turn, cache):
    if p1score >= 21:
        return 1, 0
    elif p2score >= 21:
        return 0, 1
    result = (0, 0)
    for i in range(3):
        if turn < 3:
            after_roll = position_after_roll(p1, i + 1)
            score = after_roll + p1score if turn == 2 else p1score
            next_turn1 = next_turn(turn)
            key = (after_roll, p2, score, p2score, next_turn1)
            if key in cache:
                game = cache[key]
            else:
                game = play_game(after_roll, p2, score, p2score, next_turn1, cache)
                cache[key] = game
            result = (result[0] + game[0], result[1] + game[1])
        else:
            after_roll = position_after_roll(p2, i + 1)
            score = after_roll + p2score if turn == 5 else p2score
            next_turn2 = next_turn(turn)
            key = (p1, after_roll, p1score, score, next_turn2)
            if key in cache:
                game = cache[key]
            else:
                game = play_game(p1, after_roll, p1score, score, next_turn2, cache)
                cache[key] = game
            result = (result[0] + game[0], result[1] + game[1])
    if result[0] % 1000 == 0 and result[0] > 1000:
        print(result)
    return result


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(filename, "r") as f:
        p1 = int(f.readline()[-2])
        p2 = int(f.readline()[-1])
    print(p1, p2)

    cache = {}
    result = play_game(p1, p2, 0, 0, 0, cache)
    print(result)


if __name__ == "__main__":
    main()
