import re
import concurrent.futures
import time


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
            self.levels.append([int(x) for x in map_line.split()])

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


def find_min(start, ran, thread_num, res):
    start_time = time.time()
    m = -1
    last_x = start
    for x in range(start, start+ran):
        if (x - last_x)/ran > .05:
            print(f'thread {thread_num}: {round(((last_x := x) - start) / ran * 100, 2)}%')
        if (n := seed_map.mapping_of(x)) < m or m < 0:
            m = n
    print(f'thread {thread_num} done in {time.time() - start_time} min={m}')
    res.append(m)


with open('input', 'r') as f:
    seeds = [(int(m.group(1)), int(m.group(2))) for m in re.finditer(r'(\d+) (\d+)', f.readline())]
    maps = [re.findall(r'\d+ \d+ \d+', m) for m in re.split(r'\n\w+-to-\w+ map:', f.read())]

if __name__ == '__main__':
    seed_map = Map(m := maps[1])
    for m in maps[2:]:
        seed_map.next_map(m)

    results = []
    threads = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for i, (s, r) in enumerate(seeds):
            print(f'THREAD {i} -> find_min({s}, {r})')
            threads.append(executor.submit(find_min, s, r, i, results))
    print(results)
    print(min(results))
