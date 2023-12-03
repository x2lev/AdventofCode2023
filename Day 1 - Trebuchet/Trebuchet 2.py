words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

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


if __name__ == '__main__':
    num = 0
    for line in file:
        num += 10*find_digit(line) + find_digit(line, reverse=True)

    print(num)
