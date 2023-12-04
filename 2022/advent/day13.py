import functools
from advent import Advent, runner
from advent.parser import StarParser, ParserSkip

eval_line = lambda fh: eval(next(fh))


class Day13(Advent):
    PARSER = StarParser([eval_line, eval_line, ParserSkip()])

    def part_one(self, rows):
        s = 0
        for i, (l, r) in enumerate(rows):
            print(f"== Pair {i+1} ==")
            if in_order(l, r) == True:
                print(f"Pair {i+1} is in order")
                s += i + 1
            else:
                print(f"Pair {i+1} is not in order")
            print()
        return s

    def part_two(self, rows):
        packets = [lr for pair in rows for lr in pair]
        packets.append([[2]])
        packets.append([[6]])

        sorted_packets = sorted(
            packets, key=functools.cmp_to_key(lambda x, y: -1 if in_order(x, y) else 1)
        )
        for packet in sorted_packets:
            print(packet)

        return (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)


class KeepChecking:
    pass


def in_order(left, right):
    print(f"Compare {left} vs {right}")
    match left, right:
        case int(), int():
            if left < right:
                print(f"{left} < {right} == in order")
                return True
            if left > right:
                print(f"{left} > {right} == not in order")
                return False
            # print(f"{left} == {right}")
            return KeepChecking
        case list(), int():
            print(f"Mixed types; convert right to [{right}] and retry")
            return in_order(left, [right])
        case int(), list():
            print(f"Mixed types; convert left to [{left}] and retry")
            return in_order([left], right)
        case _:
            # print(f"both lists {len(left)}, {len(right)}")
            for v in range(min(len(left), len(right))):
                check = in_order(left[v], right[v])
                if check == KeepChecking:
                    continue
                else:
                    return check
            if len(left) == len(right):
                print("didn't conclude, keep checking")
                return KeepChecking
            if len(left) < len(right):
                print("left side ran out of items so right order")
                return True
    print("Right side ran out of items so NOT right order")
    return False


runner(Day13())
