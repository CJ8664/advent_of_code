from collections import defaultdict


def __get_input_lines():
    with open("input.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh.readlines()]


sample = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

SPECIAL_CHAR_COORDS = defaultdict(list)


class SpecialChar:
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col
        self.matched_nums = list()


def check_candidate(row, cols, num):
    for r in [row, row + 1, row - 1]:
        for c in range(min(cols) - 1, max(cols) + 2):
            for special_char in SPECIAL_CHAR_COORDS[r]:
                if special_char.row == r and special_char.col == c:
                    special_char.matched_nums.append(int(num))
                    return True
    return False


def common_parsing():
    lines = __get_input_lines()
    for row, line in enumerate(lines):
        for col, ch in enumerate(line):
            if ch != "." and not ch.isdigit():
                SPECIAL_CHAR_COORDS[row].append(SpecialChar(row, col))
    for row, line in enumerate(lines):
        num = ""
        cols = set()
        for col, ch in enumerate(line):
            if ch.isdigit():
                num += ch
                cols.add(col)
            elif num != "":
                check_candidate(row, cols, num)
                num = ""
                cols = set()
        if num != "":
            check_candidate(row, cols, num)


def day_1():
    result = 0
    for _, special_chars in SPECIAL_CHAR_COORDS.items():
        for special_char in special_chars:
            for num in special_char.matched_nums:
                result += num
    print(result)


def day_2():
    result = 0
    for _, special_chars in SPECIAL_CHAR_COORDS.items():
        for special_char in special_chars:
            if len(special_char.matched_nums) == 2:
                result += special_char.matched_nums[0] * special_char.matched_nums[1]
    print(result)


def main():
    common_parsing()
    day_1()
    day_2()


if __name__ == "__main__":
    main()
