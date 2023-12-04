from advent import Advent, runner


def fully_contains(x1, y1, x2, y2):
    return x1 >= x2 and y1 <= y2


def overlaps(x1, y1, x2, y2):
    return not set(range(x1, y1 + 1)).isdisjoint(set(range(x2, y2 + 1)))


class Day04(Advent):
    def part_one(self, rows):
        # n-n,n-n
        count = 0
        for r in rows:
            p1, p2 = [[int(x) for x in p.split("-")] for p in r.split(",")]
            if fully_contains(*p1, *p2) or fully_contains(*p2, *p1):
                count += 1
        return count

    def part_two(self, rows):
        count = 0
        for r in rows:
            p1, p2 = [[int(x) for x in p.split("-")] for p in r.split(",")]
            if overlaps(*p1, *p2):
                count += 1
        return count


runner(Day04())
