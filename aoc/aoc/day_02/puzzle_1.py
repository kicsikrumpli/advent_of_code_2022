from enum import Enum
from pprint import pprint
from typing import List, Tuple

test_input = """A Y
B X
C Z"""


class Game(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

    @staticmethod
    def from_abc(letter: str):
        return Game(ord(letter) - ord('A'))

    @staticmethod
    def from_xyz(letter):
        return Game(ord(letter) - ord('X'))

    @property
    def score(self):
        return self.value + 1

    def beats(self, other: 'Game'):
        return bool(((self.value - other.value) % 3) % 2)

    def round(self, other: 'Game') -> int:
        return int(self.beats(other)) * 6 + int(self is other) * 3


def parse(lines: List[str]) -> List[Tuple[Game, Game]]:
    def make_pair(l: str):
        left, right = l.split(" ")
        return Game.from_abc(left), Game.from_xyz(right)

    return [
        make_pair(line)
        for line
        in lines
    ]


def read_file(name: str) -> List[str]:
    with open(name, 'rt') as f:
        return [line.strip() for line in f]


if __name__ == '__main__':
    # rounds = parse(test_input.split("\n"))
    rounds = parse(read_file('input.txt'))
    # pprint(rounds)
    scores = [
        me.round(other) + me.score
        for other, me
        in rounds
    ]
    # print("scores of rounds: ", scores)
    print("total score: ", sum(scores))
