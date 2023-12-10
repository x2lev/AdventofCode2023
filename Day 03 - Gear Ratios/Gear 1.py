import re
from typing import Match

with open('input', 'r') as f:
    file = f.read().splitlines()


def value_of_number(match: Match, row):
    lines = ''.join([''.join(r[max(0, match.start() - 1):min(len(file[row]), match.end() + 1)])
                     for r in file[max(0, row - 1):min(len(file), row + 2)]])
    if re.findall(r'[#$%&*+\-/=@]', lines):
        return int(match.group(0))
    return 0


if __name__ == '__main__':
    part_total = 0

    for line in file:
        part_total += sum(value_of_number(x, file.index(line)) for x in re.finditer(r'\d+', line))

    print(part_total)
