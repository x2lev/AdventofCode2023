import re

with open('input', 'r') as f:
    data = f.read()
    file = data.splitlines()


def value_of_number(num, length, row, col):
    for r in range(max(0, row - 1), min(len(file), row + 2)):
        for c in range(max(0, col - 1), min(len(file[row]), col + length + 1)):
            symbol = file[r][c]
            if symbol in ['#', '$', '%', '&', '*', '+', '-', '/', '=', '@']:
                return num
    return 0


if __name__ == '__main__':
    part_total = 0

    for line in file:
        nums = []
        temp = line
        split_line = [x for x in re.split(r'\D', line) if x != '']
        for i in range(len(split_line)):
            x = split_line[i]
            nums.append((int(x), len(x), file.index(line), temp.index(x)))
            temp = temp.replace(x, '.' * len(x), 1)

        for item in nums:
            value = value_of_number(*item)
            part_total += value

    print(part_total)
