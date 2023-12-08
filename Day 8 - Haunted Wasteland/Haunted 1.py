import re

with open('input', 'r') as f:
    instructions = f.readline()[:-1]
    node_map = {m.group(1): {'L': m.group(2), 'R': m.group(3)}
                for m in re.finditer(r'([A-Z]{3}).{4}([A-Z]{3}).{2}([A-Z]{3})', f.read())}


def steps_to_reach_zzz():
    i = 0
    node = 'AAA'
    while node != 'ZZZ':
        direction = instructions[i % len(instructions)]
        node = node_map[node][direction]
        i += 1
    return i


if __name__ == '__main__':
    print(steps_to_reach_zzz())
