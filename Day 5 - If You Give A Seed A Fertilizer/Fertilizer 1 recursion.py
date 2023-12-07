import re


class Map:
    def __init__(self, data=None):
        self.next = None
        self.levels = []
        if data:
            self.add_map_lines(data)

    def __str__(self):
        return self.levels.__str__() + '\n' + self.next.__str__() if self.next else ''

    def add_map_line(self, map_line):
        if self.next:
            self.next.add_map_line(map_line)
        else:
            self.levels.append(map_line)

    def add_map_lines(self, map_lines):
        for map_line in map_lines:
            self.add_map_line(map_line)

    def next_map(self, data=None):
        if self.next:
            self.next.next_map(data)
        else:
            self.next = Map(data)

    def mapping_of(self, value):
        for dst, src, rng in self.levels:
            if 0 <= value - src < rng:
                if self.next:
                    return self.next.mapping_of(value + dst - src)
                return value + dst - src
        if self.next:
            return self.next.mapping_of(value)
        return value


with open('input', 'r') as f:
    seeds = [int(f) for f in re.findall(r'\d+', f.readline())]
    maps = [[[int(x) for x in f.split()] for f in re.findall(r'\d+ \d+ \d+', m)]
            for m in re.split(r'\n\w+-to-\w+ map:', f.read())]

if __name__ == '__main__':
    print(maps[1])
    seed_map = Map(maps[1])

    for m in maps[2:]:
        seed_map.next_map(m)

    print('\nmin =', min(seed_map.mapping_of(s) for s in seeds))
