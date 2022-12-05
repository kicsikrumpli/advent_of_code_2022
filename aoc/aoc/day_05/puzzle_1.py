from collections import deque
from dataclasses import dataclass
from itertools import takewhile
from pprint import pprint
from typing import List, Tuple


@dataclass
class Instruction:
    steps: int
    source: int
    target: int


def read_file(name: str) -> List[str]:
    with open(name) as f:
        return [
            line.rstrip('\n')
            for line
            in f
        ]


def parse(lines: List[str]) -> Tuple[List[deque], List[Instruction]]:
    crates = list(takewhile(lambda l: '[' in l, lines))
    stack_names = lines[len(crates)]
    columns_positions = [
        char_position
        for char_position, char in enumerate(stack_names)
        if char.isnumeric()
    ]
    stacks = [
        deque(
            filter(lambda x: x != ' ',
            [
                line[position] if position < len(line) else ' '
                for line in crates
            ][::-1]
        ))
        for position in columns_positions
    ]
    instruction_list = lines[len(crates) + 2:]
    instructions = [
        Instruction(*[
            int(x)
            for x
            in instruction.replace('move ', '').replace(' from ', ',').replace(' to ', ',').split(',')
        ])
        for instruction
        in instruction_list
    ]
    return stacks, instructions


if __name__ == '__main__':
    stacks, instructions = parse(read_file('input.txt'))
    # puzzle_1
    # for instruction in instructions:
    #     source = stacks[instruction.source - 1]
    #     target = stacks[instruction.target - 1]
    #     for _ in range(instruction.steps):
    #         target.append(source.pop())

    # puzzle_2
    for instruction in instructions:
        source = stacks[instruction.source - 1]
        target = stacks[instruction.target - 1]
        # stacking_order = 1  # for moving crates one-by-one
        stacking_order = -1  # for moving crates one stack at a time
        crates_to_move = [source.pop() for _ in range(instruction.steps)][::stacking_order]
        for crate in crates_to_move:
            target.append(crate)

    top_crates = [
        stack[-1]
        for stack
        in stacks
    ]
    print('Top crates: ', "".join(top_crates))

