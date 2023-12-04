import re

with open('input', 'r') as f:
    file = f.readlines()

if __name__ == '__main__':
    score = 0

    for line in file:
        winning_numbers = [int(x) for x in re.findall(r'\d+', line[10:39])]
        your_numbers = [int(x) for x in re.findall(r'\d+', line[42:])]

        won = False
        power = -1
        for num in your_numbers:
            if num in winning_numbers:
                won = True
                power += 1
        if won:
            score += 2**power

    print(score)

