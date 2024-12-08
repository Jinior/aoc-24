from aoc_24.day1 import part1, part2

INPUT_1 = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""
OUTPUT_1 = "11"

print(INPUT_1)


def test_day1():
    assert part1(INPUT_1) == OUTPUT_1
