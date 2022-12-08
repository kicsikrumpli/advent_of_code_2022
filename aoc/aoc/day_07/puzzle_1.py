from dataclasses import dataclass, field
from typing import Generator, Dict, Union, Optional, List

test_input = r"""$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".split("\n")


@dataclass
class Node:
    name: str
    parent: Optional['Node']
    children: Dict[str, Union['Node', int]] = field(default_factory=dict)

    @property
    def size(self) -> int:
        file_sizes = sum([child for child in self.children.values() if isinstance(child, int)])
        dir_sizes = sum([child.size for child in self.children.values() if isinstance(child, Node)])
        return file_sizes + dir_sizes

    @property
    def sub_dirs(self) -> List['Node']:
        return [child for child in self.children.values() if isinstance(child, Node)]


def parse() -> Generator[Node, str, Node]:
    root = None
    current = root
    while True:
        line = yield root
        if not line:
            break

        # print(f"...received line: {line}")
        match line.split(" "):
            case ["$", "cd", "/"]:
                if root is None:
                    root = Node(name="/", parent=None)
                current = root
            case["$", "cd", ".."]:
                current = current.parent
                # print(f"go up, new current: {current.name}")
            case["$", "cd", name]:
                current = current.children[name]
                # print(f"changed dir to: {name}")
            case ["$", "ls"]:
                # print(f"next line is dir listing")
                pass
            case ["dir", dir_name]:
                # print(f"make dir: {dir_name}")
                if dir_name not in current.children:
                    current.children[dir_name] = Node(name=dir_name, parent=current)
            case [size, file_name] if size.isnumeric():
                # print(f"make file {file_name}, with size {size}")
                if file_name not in current.children:
                    current.children[file_name] = int(size)
            case _:
                raise ValueError(line)
    return root


def sum_dirs_with_max_size(root: Node, max_size: int = 100000):
    size = root.size
    if size > max_size:
        size = 0
    return size + sum([sum_dirs_with_max_size(sub_dir) for sub_dir in root.sub_dirs])


def find_all_dir_sizes(root: Node) -> List[int]:
    size = root.size
    children_sizes = [size
                      for sub_dir in root.sub_dirs
                      for size in find_all_dir_sizes(sub_dir)]
    return [size, *children_sizes]


if __name__ == '__main__':
    dir_generator = parse()
    # prime generator
    next(dir_generator)

    # feed generator
    with open('input.txt', 'rt') as f:
        # for line in test_input:
        for line in f:
            # print("->", line)
            dir_generator.send(line.strip())

    # close generator
    try:
        next(dir_generator)
    except StopIteration as e:
        dir_root: Node = e.value

    # part 1
    print(dir_root)
    print("Sum of dir sizes with max 100000 size: ", sum_dirs_with_max_size(dir_root))

    print('-' * 10)

    # part 2
    total_disk_space = 70000000
    required_disk_space = 30000000
    total_used_spce = dir_root.size
    minimum_space_to_free_up = required_disk_space - (total_disk_space - total_used_spce)
    print(f"Need at least {minimum_space_to_free_up} more space. Total used: {total_used_spce}")
    all_dir_sizes = find_all_dir_sizes(dir_root)
    all_dir_sizes_gt_min = [size for size in all_dir_sizes if size >= minimum_space_to_free_up]
    print(f"Smallest size to delete: {min(all_dir_sizes_gt_min)}")
