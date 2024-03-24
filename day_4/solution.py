from collections import deque


def __get_input_lines():
    with open("input.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh.readlines()]


sample = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def common_parsing():
    lines = __get_input_lines()
    card_match_count = {}
    for line in lines:
        card_num = int(line[: line.index(":")].split()[1])
        wining_part, actual_number_part = line[line.index(":") + 1 :].split("|")
        winning_nums = {int(num) for num in wining_part.split()}
        actual_nums = {int(num) for num in actual_number_part.split()}
        common_nums = winning_nums.intersection(actual_nums)
        card_match_count[card_num] = len(common_nums)
    return card_match_count


def part_1(card_match_count):
    result = 0
    for _card_num, match_count in card_match_count.items():
        if match_count > 0:
            result += 2 ** (match_count - 1)
    print(result)


def part_2(card_match_count):
    card_count = 0
    queue = deque()
    queue.extend(card_match_count.keys())
    while queue:
        card_num = queue.popleft()
        card_count += 1
        match_count = card_match_count[card_num]
        for i in range(card_num + 1, card_num + match_count + 1):
            queue.append(i)
    print(card_count)


def main():
    card_match_count = common_parsing()
    part_1(card_match_count)
    part_2(card_match_count)


if __name__ == "__main__":
    main()
