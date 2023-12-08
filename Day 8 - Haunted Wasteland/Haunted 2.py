import re
import math

with open('input', 'r') as f:
    instructions = f.readline()[:-1]
    node_map = {m.group(1): {'L': m.group(2), 'R': m.group(3)}
                for m in re.finditer(r'(\w{3}).{4}(\w{3}).{2}(\w{3})', f.read())}
    start_nodes = [n for n in node_map if re.match(r'..A', n)]


def steps_to_reach_z(node):
    i = 0
    while not re.match(r'..Z', node):
        direction = instructions[i % len(instructions)]
        node = node_map[node][direction]
        i += 1
    return i


if __name__ == '__main__':
    indices = [steps_to_reach_z(n) for n in start_nodes]
    print(math.lcm(*indices))
