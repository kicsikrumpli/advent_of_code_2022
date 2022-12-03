from enum import Enum
from typing import List, Tuple


class Outcome(Enum):
    """NB! enum values come from modulo arithmetic results in Hand"""
    TIE = 0
    WIN = 1
    LOSE = 2

    @staticmethod
    def parse(letter: str):
        return {
            'X': Outcome.LOSE,
            'Y': Outcome.TIE,
            'Z': Outcome.WIN
        }[letter]

    @property
    def score(self):
        return {
            Outcome.TIE: 3,
            Outcome.WIN: 6,
            Outcome.LOSE: 0
        }[self]


class Hand(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

    def play(self, other: 'Hand'):
        return Outcome((self.value - other.value) % 3)

    @property
    def score(self):
        return self.value + 1

    @staticmethod
    def hand_for_outcome_with_other(other_hand: 'Hand',
                                    my_outcome: Outcome):
        return Hand((other_hand.value + my_outcome.value) % 3)

    @staticmethod
    def parse(letter: str):
        """
        A: rock
        B: Paper
        C: Scissors
        """
        return Hand(ord(letter) - ord('A'))


def parse(lines: List[str]) -> List[Tuple[Hand, Outcome]]:
    def make_pair(l: str):
        left, right = l.split(" ")
        return Hand.parse(left), Outcome.parse(right)

    return [
        make_pair(line)
        for line
        in lines
    ]


def read_file(name: str) -> List[str]:
    with open(name, 'rt') as f:
        return [line.strip() for line in f]


test_input = """A Y
B X
C Z"""

if __name__ == '__main__':
    print(""" my_hand             | other_hand          | outcome for me""")
    print("-" * 70)
    for my_hand in (Hand.ROCK, Hand.PAPER, Hand.SCISSORS):
        for other_hand in (Hand.ROCK, Hand.PAPER, Hand.SCISSORS):
            my_outcome = my_hand.play(other_hand)
            print(f""" {my_hand:20}| {other_hand:20}| {my_outcome:20}""")

    print("=" * 70)
    print("")
    print(""" other hand          | my outcome          | my hand """)
    print("-" * 70)
    for other_hand in (Hand.ROCK, Hand.PAPER, Hand.SCISSORS):
        for my_outcome in (Outcome.TIE, Outcome.WIN, Outcome.LOSE):
            my_hand = Hand.hand_for_outcome_with_other(other_hand, my_outcome)
            print(f""" {other_hand:20}| {my_outcome:20}| {my_hand:20}| {"✔︎" if my_hand.play(other_hand) is my_outcome else "✗"}""")

    print("=" * 70)
    print("")

    # game = parse(test_input.split("\n"))
    game = parse(read_file('input.txt'))
    for other_hand, my_outcome in game:
        my_hand = Hand.hand_for_outcome_with_other(other_hand, my_outcome)
        score = my_hand.score + my_outcome.score
        print(other_hand, my_hand, my_outcome, score)

    scores = [
        Hand.hand_for_outcome_with_other(other_hand, my_outcome).score + my_outcome.score
        for other_hand, my_outcome
        in game
    ]
    print(sum(scores))