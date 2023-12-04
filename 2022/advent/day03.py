from advent import Advent, runner


def priority(item: str):
    n = ord(item.lower()) - 96
    if item.isupper():
        return n + 26
    return n


class Day03(Advent):
    def part_one(self, rows):
        s = 0
        for sack in rows:
            p1, p2 = set(sack[: len(sack) // 2]), set(sack[len(sack) // 2 :])
            common = p1.intersection(p2).pop()
            s += priority(common)
        return s

    def part_two(self, rows):
        s = 0
        while rows:
            x, y, z = rows.pop(), rows.pop(), rows.pop()
            s += priority(set(x).intersection(y, z).pop())
        return s


runner(Day03())
