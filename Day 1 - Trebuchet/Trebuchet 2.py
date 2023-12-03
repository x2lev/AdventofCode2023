words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open('input', 'r') as f:
    file = f.readlines()


def first_digit(string):
    for c in range(len(string)):
        if string[c].isnumeric():
            return int(string[c])
        else:
            for word in words:
                if string[c:min(len(string), c + len(word))] == word:
                    return words.index(word) + 1


def last_digit(string):
    for c in range(len(string) - 1, -1, -1):
        if string[c].isnumeric():
            return int(string[c])
        else:
            for word in words:
                if string[c:min(len(string), c + len(word))] == word:
                    return words.index(word)+1


if __name__ == '__main__':
    num = 0

    for line in file:
        num += 10*first_digit(line) + last_digit(line)

    print(num)
