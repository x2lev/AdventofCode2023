with open('input', 'r') as f:
    cosmos = [x[:-1] for x in f.readlines()]


def distance(galaxy1, galaxy2):
    d = 0
    for dr in range(min(galaxy1['r'], galaxy2['r']), max(galaxy1['r'], galaxy2['r'])):
        if '#' not in cosmos[dr]:
            d += 1_000_000
        else:
            d += 1
    zip_cosmos = list(zip(*cosmos))
    for dc in range(min(galaxy1['c'], galaxy2['c']), max(galaxy1['c'], galaxy2['c'])):
        if '#' not in zip_cosmos[dc]:
            d += 1_000_000
        else:
            d += 1
    return d


if __name__ == '__main__':
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
