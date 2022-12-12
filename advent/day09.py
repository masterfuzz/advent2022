from advent import Advent, runner
from advent.parser import StarParser
from time import sleep

directions = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1)}


def parse_move(fh):
    d, n = next(fh).split()
    return directions[d], int(n)


def not_touching(hx, hy, tx, ty):
    return abs(hx - tx) > 1 or abs(hy - ty) > 1


def sign(x):
    if x == 0:
        return 0
    return -1 if x < 0 else 1


class Day09(Advent):
    PARSER = StarParser(parse_move)

    def part_one(self, rows):
        head = (0, 0)
        tail = (0, 0)
        positions = {tail}
        for (x, y), n in rows:
            for _step in range(n):
                head = head[0] + x, head[1] + y
                tail = get_new_pos(head, tail)

        return len(positions)

    def part_two(self, rows):
        # import turtle

        # turtle.Screen().setup(70, 70)
        # turtle.setworldcoordinates(-25, -25, 50, 50)

        head = (0, 0)
        tails = {k + 1: (0, 0) for k in range(9)}
        # turtles = {k: turtle.Turtle() for k in range(10)}
        positions = {head}

        for (x, y), n in rows:
            print(x, y, n)
            for _step in range(n):
                head = head[0] + x, head[1] + y
                # old_tails = tails.copy()
                tails[1] = get_new_pos(head, tails[1])
                for t in range(2, 10):
                    tails[t] = get_new_pos(tails[t - 1], tails[t])
                positions.add(tails[9])
                # print_grid(head, tails, positions)

        # print(positions)
        return len(positions)


def get_new_pos(new_head, tail):
    if not_touching(*new_head, *tail):
        dx, dy = (new_head[0] - tail[0], new_head[1] - tail[1])
        # if new_head[0] == tail[0] or new_head[1] == tail[1]:
        #     return tail[0] + sign(dx), tail[1] + sign(dy)

        # else:
        #     # move diagonally
        return tail[0] + sign(dx), tail[1] + sign(dy)
    else:
        return tail


def print_grid(head, tails, positions):
    # mx = max(head[0], *[t[0] for t in tails.values()])
    # my = max(head[1], *[t[1] for t in tails.values()])
    # nx = min(head[0], *[t[0] for t in tails.values()])
    # ny = min(head[1], *[t[1] for t in tails.values()])
    mx, my = 20, 20
    nx, ny = -20, -20
    for y in range(nx, mx):
        line = ""
        for x in range(ny, my):
            ch = "."
            if head == (x, y):
                ch = "H"
            else:
                for k, v in tails.items():
                    if v == (x, y):
                        ch = str(k)
                        break
            if ch == ".":
                if (x, y) == (0, 0):
                    ch = "s"
                elif (x, y) in positions:
                    ch = "#"
            line += ch

        print(line)
    sleep(0.5)


def tests():
    def test_get_new_pos():
        # fmt:off
        cases = [
            [[(3, 1), (1, 1)], (2, 1)],
            [[ (1, 3), (1, 1)], (1, 2)],
            [[ (2,1), (1,3)], (2,2)],
            [[ (3,2), (1,3)], (2,2)],
            [[ (-1,0), (1,0)], (0,0)],
            [[(2,0), (4,1)], (3,0)]
        ]
        # fmt:on
        for case in cases:
            args, expect = case
            assert expect == get_new_pos(*args)

    test_get_new_pos()


tests()

runner(Day09())
