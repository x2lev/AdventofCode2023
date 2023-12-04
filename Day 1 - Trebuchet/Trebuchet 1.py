import re

with open('input', 'r') as f:
    file = f.readlines()


def find_digit_by_regex(line, reverse=False):
    return int(re.findall(r'\d', line)[-1 if reverse else 0])


if __name__ == '__main__':
    print(sum([10*find_digit_by_regex(line) + find_digit_by_regex(line, reverse=True) for line in file]))
