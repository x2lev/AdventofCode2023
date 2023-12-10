from PIL import Image
import numpy as np

with open('input', 'r') as f:
    maze = f.readlines()


def adjacent(curr, prev):
    r, c = curr
    pr, pc = prev
    s = maze[r][c]
    if s == '|':
        return (r + 1, c) if pr < r else (r - 1, c)
    if s == '-':
        return (r, c + 1) if pc < c else (r, c - 1)
    if s == 'L':
        return (r - 1, c) if pr == r else (r, c + 1)
    if s == 'J':
        return (r, c - 1) if pc == c else (r - 1, c)
    if s == '7':
        return (r, c - 1) if pc == c else (r + 1, c)
    if s == 'F':
        return (r + 1, c) if pr == r else (r, c + 1)
    raise ValueError(r, c)


def symbol(r, c):
    return maze[r][c]


if __name__ == '__main__':
    white = 0xFFFFFF
    black = 0x000000
    red = 0xFF0000
    pixels = []
    for ind, line in enumerate(maze):
        pixels.append([])
        for i, s in enumerate(line):
            if s == '.':
                pixels[ind].append(white)
            elif s == 'S':
                print('S', ind, i)
                pixels[ind].append(red)
            else:
                pixels[ind].append(black)
    image = Image.fromarray(np.asarray(pixels), 'I')
    image.save('maze.png')
    row, col = 0, 0
    for ind, line in enumerate(maze):
        if 'S' in line:
            row, col = (ind, line.index('S'))
            break
    current = []
    if maze[row - 1][col] in ('|', '7', 'F'):
        current.append((row - 1, col))
    if maze[row + 1][col] in ('|', 'L', 'J'):
        current.append((row + 1, col))
    if maze[row][col - 1] in ('-', 'L', 'F'):
        current.append((row, col - 1))
    if maze[row][col + 1] in ('-', 'J', '7'):
        current.append((row, col + 1))
    last = [(row, col), (row, col)]
    d = 1
    while current[0] != current[1]:
        current, last = [adjacent(current[0], last[0]), adjacent(current[1], last[1])], current
        d += 1
    print(d, symbol(*current[0]), symbol(*current[1]))
