import functools
from pprint import pprint
from typing import List, Tuple, Set

test_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


def parse(rucksacks: List[str], elf_group_size=3) -> List[Tuple[Set[str], ...]]:
    return [
        tuple([
            set(rucksack)
            for rucksack
            in rucksacks[slice_idx: slice_idx + elf_group_size]
        ])
        for slice_idx
        in range(0, len(rucksacks), elf_group_size)
    ]


def read_file(name: str) -> List[str]:
    with open(name, 'rt') as f:
        return [
            line.strip()
            for line
            in f
        ]


def priority(item: str) -> int:
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27


if __name__ == '__main__':
    # rucksacks = parse(test_input.split("\n"))

    rucksacks = parse(read_file('input.txt'))
    elf_groups = [
        left.intersection(right).intersection(middle)
        for left, middle, right
        in rucksacks
    ]
    print(elf_groups)
    sum_priorities = functools.reduce(
        lambda acc, elem: acc + priority(elem.pop()),
        elf_groups,
        0
    )
    print(sum_priorities)
