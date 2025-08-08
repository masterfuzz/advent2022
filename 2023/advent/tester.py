from io import TextIOWrapper
import os
from advent.parser import Parser, to_parser
from traceback import print_exc


class Advent:
    PARSER = None
    PARSER_2 = None

    def __init__(self) -> None:
        self.day = type(self).__name__[-2:]

    def sm_parsed(self):
        with open(f"inputs/{self.day}_small") as fh:
            return self.parse(fh)

    def parse(self, fh: TextIOWrapper):
        if self.PARSER:
            return to_parser(self.PARSER).parse(fh)
        return fh.read().splitlines()

    def parse_2(self, fh: TextIOWrapper):
        if self.PARSER_2:
            return to_parser(self.PARSER_2).parse(fh)
        return self.parse(fh)

    def test(self):
        with open(f"inputs/{self.day}_small") as fh:
            rows1 = self.parse(fh)
        with open(f"inputs/{self.day}_small") as fh:
            rows2 = self.parse_2(fh)
        ans = []
        if os.path.exists(f"answers/{self.day}_small"):
            with open(f"answers/{self.day}_small") as fh:
                ans = [int(x) for x in fh.read().splitlines()]
        p1 = ""
        p2 = ""
        a1 = self.part_one(rows1)
        a2 = self.part_two(rows2)
        if len(ans) > 0:
            if a1 == ans[0]:
                p1 = "PASSED"
            else:
                p1 = f"FAILED (should be {ans[0]})"
            if len(ans) > 1:
                if a2 == ans[1]:
                    p2 = "PASSED"
                else:
                    p2 = f"FAILED (should be {ans[1]})"
        print("Part 1", a1, p1)
        print("Part 2", a2, p2)

    def part_one(self, rows):
        return "Not implemented"

    def part_two(self, rows):
        return "Not implemented"

    def run(self, fname=None):
        if fname is None:
            fname = f"inputs/{self.day}_big"
        with open(fname) as fh:
            rows1 = self.parse(fh)
        with open(fname) as fh:
            rows2 = self.parse_2(fh)
        try:
            p1 = self.part_one(rows1)
            print("Part 1:", p1)
        except Exception as e:
            print("Part 1:")
            print_exc()

        try:
            p2 = self.part_two(rows2)
            print("Part 2:", p2)
        except Exception as e:
            print("Part 2:")
            print_exc()


def loop_parser(sub_parser, fh):
    while True:
        try:
            yield sub_parser(fh)
        except StopIteration as e:
            break


def runner(day: Advent):
    import sys

    if len(sys.argv) == 2:
        arg = sys.argv[1]
        if arg == "-":
            pass
        if arg == "big":
            day.run()
        else:
            day.run(arg)
    else:
        day.test()
