import re


with open('input', 'r') as f:
    seeds = [int(f) for f in re.findall(r'\d+', f.readline())]
    maps = [[[int(x) for x in f.split()] for f in re.findall(r'\d+ \d+ \d+', m)]
            for m in re.split(r'\n\w+-to-\w+ map:', f.read())]

if __name__ == '__main__':
    for m in maps:
        temp = []
        for seed in seeds:
            for dst, src, rng in m:
                if src <= seed < src + rng:
                    temp.append(seed - src + dst)
                    break
            else:
                temp.append(seed)
        seeds = temp

    print(min(seeds))
