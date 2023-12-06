import re
from typing import Match

with open('input', 'r') as f:
    file = f.read().splitlines()


def find_adjacent_gear(num, length, row, col):
    for r in range(max(0, row - 1), min(len(file), row + 2)):
        for c in range(max(0, col - 1), min(len(file[row]), col + length + 1)):
            symbol = file[r][c]
            if symbol == '*':
                return (r, c), num
    return None


def find_adjacent_gear_re(match, row):
    if row > 0:
        line_to_search = file[row-1][max(0, match.start() - 1):min(len(file[row]), match.end() + 1)]
        if len(find := list(re.finditer(r'\*', line_to_search))) > 0:
            return find[0], row-1
    if row < len(file)-1:
        line_to_search = file[row+1][max(0, match.start() - 1):min(len(file[row]), match.end() + 1)]
        if len(find := list(re.finditer(r'\*', line_to_search))) > 0:
            return find[0], row+1
    line_to_search = file[row][max(0, match.start() - 1):min(len(file[row]), match.end() + 1)]
    if len(find := list(re.finditer(r'\*', line_to_search))) > 0:
        return find[0], row
    return None, row


if __name__ == '__main__':
    gear_total = 0
    gear_total_re = 0

    gears = {}
    gears_re = {}
    for index in range(len(file)):
        line = file[index]
        nums = []
        temp = line
        split_line = [x for x in re.split(r'\D', line) if x != '']
        for x in re.finditer(r'\d+', line):
            g, ind = find_adjacent_gear_re(x, index)
            if g:
                gears_re.setdefault((ind, x.start()+g.start()-1), []).append(int(x.group(0)))

        for i in range(len(split_line)):
            x = split_line[i]
            nums.append((int(x), len(x), index, temp.index(x)))
            temp = temp.replace(x, '.' * len(x), 1)

        for item in nums:
            if gear := find_adjacent_gear(*item):
                rc, cog = gear
                gears.setdefault(rc, []).append(cog)

    for gear in gears.values():
        if len(gear) > 1:
            g = 1
            for cog in gear:
                g *= cog
            gear_total += g

    for gear in gears_re.values():
        if len(gear) > 1:
            g = 1
            for cog in gear:
                g *= cog
            gear_total_re += g

    for dif in dict(set({k: tuple(v) for k, v in gears.items()}) - set({k: tuple(v) for k, v in gears_re.items()})):
        print(end=f'{dif}: ')
        try:
            print(gears[dif], '->', gears_re[dif])
        except KeyError:
            print(gears[dif])

    print(gear_total)
    print(gear_total_re)
