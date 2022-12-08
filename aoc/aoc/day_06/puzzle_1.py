import collections
from typing import Iterator, Optional, Deque

test_inputs = [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11)
]


def seek_start_sequence(buff: str, num_distibct_chars=4) -> Iterator[Optional[int]]:
    buffer: Deque[Optional[str]] = collections.deque([], maxlen=num_distibct_chars)
    for idx, char in enumerate(buff):
        buffer.append(char)
        if len(set(buffer)) == num_distibct_chars:
            yield idx + 1
        else:
            yield None


if __name__ == '__main__':
    # for test_input, expected in test_inputs:
    #     print(test_input)
    #     for idx in seek_start_sequence(test_input):
    #         if idx:
    #             print(f"expected: {expected}, got: {idx}")
    #             print(test_input[:idx])
    #             break

    for seq_len in (4, 14):
        with open('input.txt', 'rt') as f:
            for idx in seek_start_sequence(f.readline(), seq_len):
                if idx:
                    print(f"start seq end position with {seq_len} long sequence: ", idx)
                    break

