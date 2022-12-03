import functools
from pprint import pprint
from typing import List, Tuple, Set

test_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


def parse(rucksacks: List[str]) -> List[Tuple[Set[str], Set[str]]]:
    return [
        (set(content[:len(content) // 2]), set(content[len(content) // 2:]))
        for content
        in rucksacks
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
    #rucksacks = parse(test_input.split("\n"))

    rucksacks = parse(read_file('input.txt'))
    misplaced_items = [
        left.intersection(right)
        for left, right
        in rucksacks
    ]
    print(misplaced_items)
    sum_priorities = functools.reduce(
        lambda acc, elem: acc + priority(elem.pop()),
        misplaced_items,
        0
    )
    print(sum_priorities)
