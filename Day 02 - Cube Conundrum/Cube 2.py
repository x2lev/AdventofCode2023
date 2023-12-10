import re

with open('input', 'r') as f:
    file = f.readlines()


def power_of_max_cubes(t):
    max_cubes = {'red': 0, 'green': 0, 'blue': 0}
    for trial in t:
        for color in max_cubes:
            if color in trial and trial[color] > max_cubes[color]:
                max_cubes[color] = trial[color]
    power = 1
    for n in max_cubes.values():
        power *= n
    return power


if __name__ == '__main__':
    total_power = 0

    game = 0
    for line in file:
        game += 1
        trials = [{match.group(2): int(match.group(1)) for match in re.finditer(r'(\d+) (red|green|blue)', trial)}
                  for trial in line[len(f'Game {game}: '):-1].split('; ')]
        total_power += power_of_max_cubes(trials)

    print(total_power)
