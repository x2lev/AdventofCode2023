import re

with open('input', 'r') as f:
    file = f.readlines()
words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def find_digit_by_regex(line, reverse=False):
    match = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)[-1 if reverse else 0]
    return int(match) if match.isnumeric() else (words.index(match)+1)


if __name__ == '__main__':
    print(sum([10 * find_digit_by_regex(line) + find_digit_by_regex(line, reverse=True) for line in file]))
