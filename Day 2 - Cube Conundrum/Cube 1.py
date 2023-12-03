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
        trials = line[len(f'Game {game}: '):-1].split('; ')
        trials = [{c: int(n) for n, c in [cube.split() for cube in cubes.split(', ')]} for cubes in trials]
        if does_not_exceed_max(trials):
            game_total += game

    print(game_total)
