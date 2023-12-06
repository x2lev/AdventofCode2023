class Map:
    def __init__(self):
        self.levels = []
        self.next = None

    def __str__(self):
        return self.levels.__str__() + '\n' + self.next.__str__() if self.next else ''

    def add_map_line(self, map_line):
        if self.next:
            self.next.add_map_line(map_line)
        else:
            self.levels.append([int(x) for x in map_line.split()])

    def next_map(self):
        if self.next:
            self.next.next_map()
        else:
            self.next = Map()

    def mapping_of(self, value):
        mapping = value
        for dst, src, rng in self.levels:
            if 0 <= (dif := value - src) < rng:
                mapping = dst + dif
        if self.next:
            return self.next.mapping_of(mapping)
        return mapping


with open('input', 'r') as f:
    file = f.readlines()

if __name__ == '__main__':
    seeds = []
    seed_map = None
    for index in range(len(file)):
        line = file[index]
        if 'seeds' in line:
            seeds = [int(s) for s in line[7:].split()]
        elif line == '\n':
            if seed_map:
                seed_map.next_map()
            else:
                seed_map = Map()
        elif 'map' not in line:
            seed_map.add_map_line(line)

    print(seed_map)
    for seed in seeds:
        print(seed_map.mapping_of(seed))
    print('\nmin =', min(seed_map.mapping_of(s) for s in seeds))
