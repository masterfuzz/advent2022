from advent import Advent, runner
from advent.parser import StarParser


def parse_instruction(fh):
    x, *y = next(fh).split()
    if y:
        return x, int(y[0])
    return x, 0


def signal_strength(cycle, x):
    if (cycle - 20) % 40 == 0:
        # print(f"cool signal {cycle*x} at {cycle}")
        return cycle * x
    return 0


class Day10(Advent):
    PARSER = StarParser(parse_instruction)

    def part_one(self, rows):
        x = 1
        cycle = 0
        signal = 0
        for ins, val in rows:
            cycle += 1
            signal += signal_strength(cycle, x)
            if ins == "noop":
                continue
            cycle += 1
            signal += signal_strength(cycle, x)
            x += val
        return signal

    def part_two(self, rows):
        width, height = 40, 6
        crt = [["." for _x in range(width)] for _y in range(height)]

        x = 1
        cycle = 0
        for ins, val in rows:
            draw(crt, cycle, x)
            cycle += 1
            if ins == "noop":
                continue
            draw(crt, cycle, x)
            cycle += 1
            x += val

            print("\n".join(["".join(row) for row in crt]))
            print()


def draw(crt, cycle, x):
    crt_x, crt_y = cycle % 40, cycle // 40
    sprite = [x + i - 1 for i in range(3)]

    if crt_x in sprite:
        print(f"DRAW cycle={cycle} row={crt_y} col={crt_x} sprite={sprite}")
        crt[crt_y][crt_x] = "#"
    else:
        print(f"NOPE cycle={cycle} row={crt_y} col={crt_x} sprite={sprite}")
        # crt[crt_y][crt_x] = "."


runner(Day10())
