def part_1():
    result = 0
    with open("input.txt", "r") as fh:
        for line in fh.readlines():
            digits = [int(char) for char in line.strip() if char.isnumeric()]
            result += digits[0] * 10 + (digits[-1] if len(digits) > 1 else digits[0])
        print(result)


def part_2():
    result = 0
    num_map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    start_chrs = {k[0] for k in num_map}
    with open("input.txt", "r") as fh:
        for line in [l.strip() for line in fh.readlines()]:
            digits = []
            for idx, char in enumerate(line):
                if char.isnumeric():
                    digits.append(int(char))
                elif char in start_chrs:
                    for i in [3, 4, 5]:
                        if line[idx : idx + i] in num_map:
                            digits.append(num_map[line[idx : idx + i]])
            result += digits[0] * 10 + (digits[-1] if len(digits) > 1 else digits[0])
    print(result)


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
