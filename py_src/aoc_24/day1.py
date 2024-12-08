import heapq

from aoc_24.utils import get_day_input


def _parse_input(input: str) -> tuple[list[int], list[int]]:
    list1 = []
    list2 = []
    for line in input.splitlines():
        left, right = line.split()
        list1.append(int(left))
        list2.append(int(right))
    return list1, list2


def part1(input) -> str:
    heap1, heap2 = _parse_input(input)
    heapq.heapify(heap2)
    heapq.heapify(heap1)

    if len(heap1) != len(heap2):
        raise ValueError(
            "Number lists are not of same length. There is either an issue with the input or parsing."
        )

    result = 0
    for _ in range(len(heap1)):
        result += abs(heapq.heappop(heap1) - heapq.heappop(heap2))
    return str(result)


def part2(input) -> str:
    return ""


def main() -> None:
    print("Day 1")
    print(f"Solution to part 1: {part1(get_day_input(1, 1))}")
    # print(f"Solution to part 2: {part1(get_day_input(1, 2))}")


if __name__ == "__main__":
    main()
