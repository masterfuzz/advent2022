import operator
from advent import Advent, runner
from advent.parser import StarParser, ParserSkip

ops = {"+": operator.add, "*": operator.mul}


class Monkey:
    def __init__(self, fh) -> None:
        self.name = next(fh)
        self.items = list(map(int, next(fh).split(": ")[-1].split(", ")))

        self.operation_expr = next(fh).split(": ")[-1].split("=")[-1].split()

        self.test_value = int(next(fh).split("by ")[-1])

        self.if_true = int(next(fh).split()[-1])
        self.if_false = int(next(fh).split()[-1])

        self.inspections = 0

    def test(self, item):
        return item % self.test_value == 0

    def operation(self, old):
        l, op, r = self.operation_expr
        if l == "old":
            l = old
        else:
            l = int(l)
        if r == "old":
            r = old
        else:
            r = int(r)
        if not type(r) == int or not type(l) == int:
            print("wat")
        return ops[op](l, r)

    def take_turn(self, other_monkeys: list["Monkey"], factor=None):
        for item in self.items:
            self.inspections += 1
            item = self.operation(item)
            if factor:
                item = item % factor
            else:
                item = item // 3
            if self.test(item):
                other_monkeys[self.if_true].items.append(item)
            else:
                other_monkeys[self.if_false].items.append(item)
        self.items = []


class Day11(Advent):
    PARSER = StarParser(Monkey, ParserSkip())

    def part_one(self, monkeys: list[Monkey]):
        for monkey in monkeys:
            print(monkey.__dict__)
        for _round in range(20):
            for monkey in monkeys:
                monkey.take_turn(monkeys)

        *_, m1, m2 = sorted([m.inspections for m in monkeys])
        return m1 * m2

    def part_two(self, monkeys):
        factor = 1
        for m in monkeys:
            factor *= m.test_value

        for _round in range(10000):
            for monkey in monkeys:
                monkey.take_turn(monkeys, factor)

        *_, m1, m2 = sorted([m.inspections for m in monkeys])
        return m1 * m2


runner(Day11())
