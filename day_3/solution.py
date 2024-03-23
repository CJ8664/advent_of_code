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

SPECIAL_CHAR_COORDS = set()


def check_candidate(row, cols):
    for r in [row, row + 1, row - 1]:
        for c in range(min(cols) - 1, max(cols) + 2):
            if (r, c) in SPECIAL_CHAR_COORDS:
                return True
    return False


def day_1():
    lines = __get_input_lines()
    for row, line in enumerate(lines):
        for col, ch in enumerate(line):
            if ch != "." and not ch.isdigit():
                SPECIAL_CHAR_COORDS.add((row, col))

    result = 0
    for row, line in enumerate(lines):
        num = ""
        cols = set()
        for col, ch in enumerate(line):
            if ch.isdigit():
                num += ch
                cols.add(col)
            elif num != "":
                if check_candidate(row, cols):
                    result += int(num)
                num = ""
                cols = set()
        if num != "":
            if check_candidate(row, cols):
                result += int(num)

    print(result)


def day_2():
    lines = __get_input_lines()


def main():
    day_1()
    day_2()


if __name__ == "__main__":
    main()
