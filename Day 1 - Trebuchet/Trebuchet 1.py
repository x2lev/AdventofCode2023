with open('input', 'r') as f:
    file = f.readlines()


def find_digit(string, reverse=False):
    for c in range(len(string) - 1, -1, -1) if reverse else range(len(string)):
        if string[c].isnumeric():
            return int(string[c])


if __name__ == '__main__':
    num = 0

    for line in file:
        num += 10*find_digit(line) + find_digit(line, reverse=True)

    print(num)
