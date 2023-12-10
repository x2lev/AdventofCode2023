import re

with open('input', 'r') as f:
    seed_ranges = [(int(m.group(1)), int(m.group(2))) for m in re.finditer(r'(\d+) (\d+)', f.readline())]
    maps = [[[int(x) for x in f.split()] for f in re.findall(r'\d+ \d+ \d+', m)]
            for m in re.split(r'\n\w+-to-\w+ map:', f.read())]

if __name__ == '__main__':
    for m in maps:
        temp = []
        while seed_ranges:
            s, r = seed_ranges.pop()
            for dst, src, rng in m:
                if (start := max(s, src)) < (end := min(s + r, src + rng)):
                    temp.append((start - src + dst, end - start))
                    if start > s:
                        seed_ranges.append((s, start - s))
                    if end < s + r:
                        seed_ranges.append((end, s + r - end))
                    break
            else:
                temp.append((s, r))
        seed_ranges = temp

    print(min(seed_ranges))
