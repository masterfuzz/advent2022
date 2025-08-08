from . import Advent, runner
from .parser import ParserSkip, StarParser


class Node:
    def __init__(self, fh):
        s = next(fh).strip()
        if not s:
            raise StopIteration()
        self.name, self.left, self.right = "".join(c for c in s if c not in '=,()').split()

    def __repr__(self):
        return f"{self.name} = ({self.left}, {self.right})"



class Day08(Advent):
    PARSER = [lambda fh: next(fh).strip(),
              ParserSkip(),
              StarParser(Node)]

    def part_one(self, rows):
        inst, nodes = rows
        mapping = {node.name: node for node in nodes}

        pos = mapping['AAA']
        step = 0
        while pos.name != 'ZZZ':
            pos = mapping[pos.left if inst[step % len(inst)] == 'L' else pos.right]
            step += 1
        return step

    def part_two(self, rows):
        inst, nodes = rows
        mapping = {node.name: node for node in nodes}

        positions = [mapping[node.name] for node in nodes if node.name[-1] == 'A']
        step = 0
        while any(node.name[-1] != 'Z' for node in positions):
            positions = [
                mapping[pos.left if inst[step % len(inst)] == 'L' else pos.right]
                for pos in positions
            ]
            step += 1
        return step


runner(Day08())
