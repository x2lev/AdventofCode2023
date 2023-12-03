import re

words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
words_regex = r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))'

with open('input', 'r') as f:
    file = f.readlines()


def find_digit(string, reverse=False):
    for c in range(len(string) - 1, -1, -1) if reverse else range(len(string)):
        if string[c].isnumeric():
            return int(string[c])
        else:
            for word in words:
                if string[c:min(len(string), c + len(word))] == word:
                    return words.index(word) + 1


def find_digit_by_regex(string, reverse=False):
    match = re.findall(words_regex, string)[-1 if reverse else 0]
    return int(match) if match.isnumeric() else (words.index(match)+1)


if __name__ == '__main__':
    num = 0
    num_re = 0

    for line in file:
        num += 10*find_digit(line) + find_digit(line, reverse=True)
        num_re += 10*find_digit_by_regex(line) + find_digit_by_regex(line, reverse=True)

    print(num)
    print(num_re)
