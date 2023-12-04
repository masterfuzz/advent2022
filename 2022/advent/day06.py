from advent import Advent, runner


class Day06(Advent):
    def part_one(self, rows):
        row = rows[0]

        for i in range(len(row) - 4):
            if len(set(row[i : i + 4])) == 4:
                return i + 4

    def part_two(self, rows):
        row = rows[0]

        for i in range(len(row) - 14):
            if len(set(row[i : i + 14])) == 14:
                return i + 14


runner(Day06())
