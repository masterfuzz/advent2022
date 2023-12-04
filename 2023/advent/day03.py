import math
from . import Advent, runner

def has_adjacent_symbol(grid, x, y):
    # for i in range(max(0, x-1), min(len(grid), x+1)):
    #     for j in range(max(0, y-1), min(len(grid[0]), y+1)):
    for i in [x-1,x,x+1]:
        if i < 0 or i >= len(grid): continue
        for j in [y-1,y,y+1]:
            if j < 0 or j >= len(grid[i]): continue

            if grid[i][j] == '.':
                continue
            if ord(grid[i][j]) in range(48,58):
                continue
            return True
    return False

def get_num_positions(grid):
    nums = []
    for x, row in enumerate(grid):
        cur = None
        for y, c in enumerate(row):
            if ord(c) in range(48,58):
                if cur:
                    cur.append([x,y])
                    continue
                cur = [[x,y]]
                continue

            if not cur:
                continue

            nums.append(cur)
            cur = None
            continue
        if cur:
            nums.append(cur)
    return nums

def adjacent_numbers(grid, nums, x, y):
    adj = []
    for i in [x-1,x,x+1]:
        if i < 0 or i >= len(grid): continue
        for j in [y-1,y,y+1]:
            if j < 0 or j >= len(grid[i]): continue
            for n in nums:
                if [i,j] in n:
                    adj.append(n)
                    continue
    return adj



def get_num(grid, xys):
    return int("".join([grid[x][y] for x, y in xys]))

class Day03(Advent):
    def part_one(self, rows):
        grid = list(map(list,rows))
        # mask = [[None for y in x] for x in grid]

        nums = get_num_positions(grid)
        print(nums)
        print([get_num(grid, xys) for xys in nums])

        total = 0
        for num in nums:
            n = get_num(grid, num)
            if any(has_adjacent_symbol(grid, x, y) for x, y in num):
                print("good:", n)
                total += n
            else:
                print("bad:", n)

        return total

    def part_two(self, rows):
        grid = list(map(list,rows))

        nums = get_num_positions(grid)
        total = 0
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c != '*': continue

                adj = adjacent_numbers(grid, nums, i, j)
                adj = set(get_num(grid, xys) for xys in adj)
                if adj and len(adj) == 2:
                    print(i, j, "good", adj)
                    ratio = math.prod(adj)
                    total += ratio
                else:
                    print(i, j, "bad", adj)

        return total

d3 = Day03()
runner(d3)
