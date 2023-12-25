import re

with open('input', 'r') as file:
    notes = [re.findall(r'[#.]+(?=\n)', sec + '\n') for sec in file.read().split('\n\n')]


def one_dif(line1, line2):
    dif = False
    for char1, char2 in zip(line1, line2):
        if char1 != char2:
            if dif:
                return False
            dif = True
    return True


def extra_value(sec: list):
    mids = []
    difference = False
    for i in range(1, len(sec)):
        if sec[i - 1] == sec[i] or (difference := one_dif(sec[i-1], sec[i])):
            mids.append(i)
    for mid in mids:
        for i in range(1, min(len(sec) - mid, mid)):
            f = mid - i - 1
            b = mid + i
            if sec[f] != sec[b] and not difference and one_dif(sec[f], sec[b]):
                break
            difference = difference or one_dif(sec[f], sec[b])
        else:
            print(mid, end=' ')
            if difference:
                return mid
    return -1


if __name__ == '__main__':
    total = 0
    for section in notes:
        print(notes.index(section))
        num1 = extra_value(list(zip(*section)))
        num2 = extra_value(section)
        print(num1, num2)
        total += num1 if -1 < num1 else 100*num2
    print(total)
