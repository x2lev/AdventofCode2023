import re

with open('input', 'r') as f:
    file = f.readlines()
max_cubes = {'red': 12, 'green': 13, 'blue': 14}


def does_not_exceed_max(t):
    for trial in t:
        for cube in max_cubes:
            if cube in trial and max_cubes[cube] < trial[cube]:
                return False
    return True


if __name__ == '__main__':
    game_total = 0

    game = 0
    for line in file:
        game += 1
        trials = [{match.group(2): int(match.group(1)) for match in re.finditer(r'(\d+) (red|green|blue)', trial)}
                  for trial in line[len(f'Game {game}: '):-1].split('; ')]
        if does_not_exceed_max(trials):
            game_total += game

    print(game_total)
