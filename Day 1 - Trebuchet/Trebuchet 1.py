import re

with open('input', 'r') as f:
    file = f.readlines()


def find_digit(string, reverse=False):
    for c in range(len(string) - 1, -1, -1) if reverse else range(len(string)):
        if string[c].isnumeric():
            return int(string[c])


def find_digit_by_regex(string, reverse=False):
    return int(re.findall(r'\d', string)[-1 if reverse else 0])


if __name__ == '__main__':
    num = 0
    num_re = 0
    for line in file:
        num += 10*find_digit(line) + find_digit(line, reverse=True)
        num_re += 10*find_digit_by_regex(line) + find_digit_by_regex(line, reverse=True)

    print(num)
    print(num_re)
