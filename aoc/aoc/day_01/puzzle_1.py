from functools import reduce
from typing import Optional, List

test_input = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def parse_from_file(name: str) -> List[Optional[int]]:
    with open(name, 'rt') as f:
        lines = f.readlines()

    return [
        int(line.strip()) if line.strip() else None
        for line
        in lines
    ]


def parse(input: str):
    lines = input.split("\n")
    if not lines[0]:
        lines = lines[1:]
    if not lines[-1]:
        lines = lines[:-1]
    return [int(line.strip()) if line.strip() else None
            for line
            in lines]


def calories_by_elf(calories: List[Optional[int]]):
    def add_to_group(acc, elem):
        if not acc:
            acc = [0]

        if elem:
            acc[-1] += elem
        else:
            acc.append(0)
        return acc

    return reduce(add_to_group, calories, [])


if __name__ == '__main__':
    # calories = parse(test_input)
    calories = parse_from_file('input.txt')
    print("Calories carried by the elves: ", calories)
    calorie_sums = calories_by_elf(calories)
    print("Total calories carried by each elf", calorie_sums)
    print("Max calories carried by a single elf", max(calorie_sums))

    sorted_calories = sorted(calorie_sums, reverse=True)
    top_three_calories = sorted_calories[:3]
    print("Sum of top 3 calories: ", sum(top_three_calories))