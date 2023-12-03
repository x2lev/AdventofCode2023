with open('input', 'r') as f:
    file = f.readlines()


def first_digit(string):
    for c in range(len(string)):
        if string[c].isnumeric():
            return int(string[c])


def last_digit(string):
    for c in range(len(line)-1, -1, -1):
        if string[c].isnumeric():
            return int(string[c])


if __name__ == '__main__':
    num = 0

    for line in file:
        num += 10*first_digit(line) + last_digit(line)

    print(num)
