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
    game_total_re = 0

    game = 0
    for line in file:
        game += 1
        trials = line[len(f'Game {game}: '):-1].split('; ')
        trials_re = [{(s := match.split())[1]: int(s[0]) for match in re.findall(r'\d+ (?:red|green|blue)', trial)} for
                     trial in trials]
        trials = [{c: int(n) for n, c in [cube.split() for cube in cubes.split(', ')]} for cubes in trials]
        if game == 1:
            print(trials_re)
            print(trials)
        if does_not_exceed_max(trials):
            game_total += game
        if does_not_exceed_max(trials_re):
            game_total_re += game

    print(game_total)
    print(game_total_re)
