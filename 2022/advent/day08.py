from advent import Advent, runner
from advent.parser import StarParser


class Day08(Advent):
    PARSER = StarParser(lambda fh: list(map(int, next(fh).strip())))

    def part_one(self, rows):
        count = 0
        for i in range(len(rows)):
            for j in range(len(rows[0])):
                if visible(rows, i, j):
                    count += 1
        return count

    def part_two(self, rows):
        best = 0
        for i in range(len(rows)):
            for j in range(len(rows[0])):
                score = scenic_score(rows, i, j)
                print(score)
                if score > best:
                    best = score
        return best


def visible(trees, i, j):
    if i == 0 or j == 0 or i == len(trees) - 1 or j == len(trees[0]) - 1:
        return True

    # horizontal
    if all(trees[i][jj] < trees[i][j] for jj in range(0, j)) or all(
        trees[i][jj] < trees[i][j] for jj in range(j + 1, len(trees[i]))
    ):
        return True

    # vertical
    if all(trees[ii][j] < trees[i][j] for ii in range(0, i)) or all(
        trees[ii][j] < trees[i][j] for ii in range(i + 1, len(trees[j]))
    ):
        return True
    return False


def line_of_sight(trees, i, j, dx, dy):

    count = 0
    my_tree = trees[i][j]
    i += dx
    j += dy
    while i >= 0 and j >= 0 and i < len(trees) and j < len(trees[0]):
        if trees[i][j] < my_tree:
            count += 1
        if trees[i][j] >= my_tree:
            return count + 1
        i += dx
        j += dy
    return count


def scenic_score(trees, i, j):
    score = 1
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        score *= line_of_sight(trees, i, j, dx, dy)
    return score


runner(Day08())
