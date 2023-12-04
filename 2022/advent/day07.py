from advent import Advent, runner


class Day07(Advent):
    def part_one(self, rows):
        root = tree(rows)
        sizes = [d.total_size() for d in root.flatten()]
        return sum(v for v in sizes if v <= 100000)

    def part_two(self, rows):
        root = tree(rows)
        used_space = root.total_size()
        free_space = 70000000 - used_space
        needed = 30000000 - free_space
        print(needed)

        smallest_sz = 70000000
        for d in root.flatten():
            sz = d.total_size()
            if sz < needed:
                continue
            if sz < smallest_sz:
                smallest_sz = sz
        return smallest_sz


def tree(cmds):
    root = Directory("/")
    cwd = root
    for cmd in cmds[1:]:
        if cmd == "$ ls":
            continue
        if ".." in cmd:
            cwd = cwd.parent
            continue
        if "$ cd" in cmd:
            dirname = cmd.split()[-1]
            cwd = cwd.sub_dirs[dirname]
            continue
        if "dir" in cmd:
            dirname = cmd.split()[-1]
            cwd.sub_dirs[dirname] = Directory(dirname, cwd)
            continue
        cwd.files += int(cmd.split()[0])
    return root


class Directory:
    def __init__(self, name: str, parent=None) -> None:
        self.parent = parent
        self.name = name
        self.sub_dirs: dict[Directory] = {}
        self.files: int = 0

    def total_size(self):
        return self.files + sum(d.total_size() for d in self.sub_dirs.values())

    def flatten(self):
        yield from self.sub_dirs.values()
        for d in self.sub_dirs.values():
            yield from d.flatten()


runner(Day07())
