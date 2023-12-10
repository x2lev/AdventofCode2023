import math
import re

with open('input', 'r') as f:
    races = zip(*[map(int, re.findall(r'\d+', x)) for x in f.readlines()])

if __name__ == '__main__':
    result = 1

    for i, (t, d) in enumerate(races):
        sqrt = math.sqrt(math.pow(t, 2)-4*d)
        hold = [round(x, 3) for x in ((t-sqrt)/2, (t+sqrt)/2) if x < t]
        options = math.ceil(hold[1])-math.floor(hold[0])-1
        print(f'time={t}, dist={d}, hold={hold}, options={options}')
        result *= options

    print(result)
