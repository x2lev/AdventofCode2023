import re

with open('input', 'r') as f:
    file = f.readlines()

if __name__ == '__main__':
    cards = [1 for _ in range(len(file))]

    for i in range(len(file)):
        print(i)
        line = file[i]
        winning_numbers = [int(x) for x in re.findall(r'\d+', line[10:39])]
        your_numbers = [int(x) for x in re.findall(r'\d+', line[42:])]
        won = 0
        for num in your_numbers:
            if num in winning_numbers:
                won += 1
        for c in range(i+1, i+won+1):
            cards[c] += cards[i]

    print(sum(cards))

