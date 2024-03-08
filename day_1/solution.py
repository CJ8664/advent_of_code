def main():
    result = 0
    with open("input.txt", "r") as fh:
        for line in fh.readlines():
            digits = [int(char) for char in line.strip() if char.isnumeric()]
            result += digits[0] * 10 + (digits[-1] if len(digits) > 1 else digits[0])
        print(result)

if __name__ == "__main__":
    main()