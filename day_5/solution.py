from collections import deque


def __get_input_lines():
    with open("input.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh.readlines()]


sample = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def common_parsing():
    lines = __get_input_lines()
    return lines


def part_1(card_match_count):
    pass


def part_2(card_match_count):
    pass


def main():
    card_match_count = common_parsing()
    part_1(card_match_count)
    part_2(card_match_count)


if __name__ == "__main__":
    main()
