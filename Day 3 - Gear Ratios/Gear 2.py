import re

with open('input', 'r') as f:
    data = f.read()
    file = data.splitlines()


def find_adjacent_gear(num, length, row, col):
    for r in range(max(0, row - 1), min(len(file), row + 2)):
        for c in range(max(0, col - 1), min(len(file[row]), col + length + 1)):
            symbol = file[r][c]
            if symbol == '*':
                return (r, c), num
    return None


if __name__ == '__main__':
    gear_total = 0

    gears = {}
    for line in file:
        nums = []
        temp = line
        split_line = [x for x in re.split(r'\D', line) if x != '']
        for i in range(len(split_line)):
            x = split_line[i]
            nums.append((int(x), len(x), file.index(line), temp.index(x)))
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

    print(gear_total)
