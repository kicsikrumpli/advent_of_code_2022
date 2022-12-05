from typing import List, Tuple

test_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def parse(l: List[str]) -> List[Tuple[range, ...]]:
    return [
        tuple([
            range(int(r.split("-")[0]), int(r.split("-")[1]) + 1)
            for r
            in line.split(',')
        ])
        for line
        in l
    ]


def read_file(name: str) -> List[str]:
    with open(name, 'rt') as f:
        return [
            line.strip()
            for line
            in f
        ]


def fully_contains(range_a: range, range_b: range) -> bool:
    return (range_a.start <= range_b.start and range_a.stop >= range_b.stop) or \
           (range_a.start >= range_b.start and range_a.stop <= range_b.stop)


def overlaps(range_a: range, range_b: range) -> bool:
    return fully_contains(range_a, range_b) or \
           range_a.start in range_b or \
           range_a.stop - 1 in range_b


if __name__ == '__main__':
    # ranges = parse(test_input.split("\n"))
    ranges = parse(read_file('input.txt'))
    no_of_fully_contained_range_pairs = sum([
        int(fully_contains(*range_pair))
        for range_pair
        in ranges
    ])
    print("Number of fully contained ranges: ", no_of_fully_contained_range_pairs)
    no_of_overlapping_range_pairs = sum([
        int(overlaps(*range_pair))
        for range_pair
        in ranges
    ])
    print("Number of overlapping ranges: ", no_of_overlapping_range_pairs)
