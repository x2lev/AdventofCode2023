with open('input', 'r') as f:
    data = [[int(x) for x in line.split()] for line in f.readlines()]

if __name__ == '__main__':
    oasis = 0
    for history in data:
        i = 0
        while not all(x == 0 for x in history):
            oasis += history[0] if i % 2 == 0 else -history[0]
            temp = []
            while len(history) > 1:
                temp.append(history[1] - history.pop(0))
            history = temp
            i += 1
    print(oasis)
 