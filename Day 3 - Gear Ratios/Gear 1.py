import re
from typing import Match

with open('input', 'r') as f:
    file = f.read().splitlines()


def value_of_number_old(num, length, row, col):
    for r in range(max(0, row - 1), min(len(file), row + 2)):
        for c in range(max(0, col - 1), min(len(file[row]), col + length + 1)):
            symbol = file[r][c]
            if symbol in ['#', '$', '%', '&', '*', '+', '-', '/', '=', '@']:
                return num
    return 0


def value_of_number(match: Match, row):
    lines = ''.join([''.join(r[max(0, match.start() - 1):min(len(file[row]), match.end() + 1)])
                     for r in file[max(0, row - 1):min(len(file), row + 2)]])
    if re.match('[#$%&*+-/=@]', lines):
        return match, lines
    return 0, lines


if __name__ == '__main__':
    part_total = 0
    part_total_re = 0

    for line in file:
        nums = []
        temp = line
        split_line = [x for x in re.split(r'\D', line) if x != '']
        regex_line = [x for x in re.finditer(r'\d+', line)]

        for split, regex in zip(split_line, regex_line):
            item = (int(split), len(split), file.index(line), temp.index(split))
            temp = temp.replace(split, '.' * len(split), 1)
            value = value_of_number_old(*item)
            match_re, lines = value_of_number(regex, file.index(line))
            value_re = 0 if match_re == 0 else int(match_re.group(0))
            if value != value_re or file.index(line) == 0:
                print(f'{lines} -> {match_re}')
                if file.index(line) > 0:
                    print(file[file.index(line) - 1])
                print(line)
                if file.index(line) < len(file)-1:
                    print(file[file.index(line) + 1])
            part_total += value
            part_total_re += value_re

    print(part_total)
    print(part_total_re)
