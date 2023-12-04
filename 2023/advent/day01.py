from .parser import StarParser
from . import Advent, runner
import regex as re

def things(row):
    nums = [x for x in row if ord(x) in range(48,58)]
    if not nums: return 0
    return int(nums[0]+nums[-1])

names = {"one": 1, "two": 2, "three": 3,
         "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0,
         **{str(n): n for n in range(10)}
         }

digit_class = "|".join(names.keys())
def digitify(row):
    digits = re.findall(f"({digit_class})", row, overlapped=True)
    if not digits: return 0
    return 10*names[digits[0]]+names[digits[-1]]

def digitify2(row):
    found_digits = []
    for i in range(len(row)):
        for n in names.keys():
            if len(row[i:]) >= len(n):
                if row[i:i+len(n)] == n:
                    found_digits.append(names[n])

    if not found_digits: return 0
    print(found_digits)
    return 10*found_digits[0] + found_digits[-1]

import random
for _ in range(1000):
    tester = random.choices([*names.keys(), "asdf"], k=random.randint(1,20))
    tester_filtered = [names[x] for x in tester if x in names]
    if not tester_filtered: continue
    tester_value = 10*tester_filtered[0]+tester_filtered[-1]
    assert tester_value == digitify("".join(tester))
    if tester_value != digitify2("".join(tester)):
        print(tester, digitify2("".join(tester)), tester_value)




class Day01(Advent):
    # PARSER = StarParser(things)
    def part_one(self, rows):
        rows = [things(row) for row in rows]
        for r in rows:
            print(r)
        return sum(rows)

    def part_two(self, rows):
        rows = [digitify2(row) for row in rows]
        for r in rows:
            print(r)
        return sum(rows)

runner(Day01())


