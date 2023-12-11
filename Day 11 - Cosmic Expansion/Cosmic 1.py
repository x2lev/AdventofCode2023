with open('input', 'r') as f:
    cosmos = [x[:-1] for x in f.readlines()]


def distance(galaxy1, galaxy2):
    return abs(galaxy1['r'] - galaxy2['r']) + abs(galaxy1['c'] - galaxy2['c'])


if __name__ == '__main__':
    cosmos = list(zip(*cosmos))
    for i, line in (e := enumerate(cosmos)):
        if '#' not in line:
            cosmos.insert(i, line)
            e.__next__()
    cosmos = list(zip(*cosmos))
    for i, line in (e := enumerate(cosmos)):
        if '#' not in line:
            cosmos.insert(i, line)
            e.__next__()
    galaxies = []
    for r, row in enumerate(cosmos):
        for c, space in enumerate(row):
            if space == '#':
                print(end='\033[35m#')
                galaxies.append({'r': r, 'c': c})
            else:
                print(end='\033[34m.')
        print()
    galaxy_pairs = []
    for i1, g1 in enumerate(galaxies):
        for i2, g2 in enumerate(galaxies[i1 + 1:]):
            galaxy_pairs.append([g1, g2])
    print(f'\033[93m{sum(distance(*gp) for gp in galaxy_pairs)}')
