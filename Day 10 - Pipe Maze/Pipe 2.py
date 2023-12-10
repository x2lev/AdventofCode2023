import sys

with open('input', 'r') as f:
    maze = f.readlines()
    cells = {(i // len(maze[0]), i % len(maze[0])): '' for i in range(len(maze) * len(maze[0]))}


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


def neighbours(curr, prev):
    r, c = curr
    pr, pc = prev
    s = maze[r][c]
    if s == '|':
        a, b = ((r, c + 1), (r, c - 1)) if pr < r else ((r, c - 1), (r, c + 1))
        if a in cells and cells[a] == '':
            cells[a] = 'A'
        if b in cells and cells[b] == '':
            cells[b] = 'B'
    elif s == '-':
        a, b = ((r, c), (r, c - 1)) if pc < c else ((r, c - 1), (r, c + 1))
        if a in cells and cells[a] == '':
            cells[a] = 'A'
        if b in cells and cells[b] == '':
            cells[b] = 'B'
    elif s == 'L':
        cell_type = 'A' if pr == r else 'B'
        cell1, cell2 = (r, c - 1), (r + 1, c)
        if cell1 in cells and cells[cell1] == '':
            cells[cell1] = cell_type
        if cell2 in cells and cells[cell2] == '':
            cells[cell2] = cell_type
    elif s == 'J':
        cell_type = 'A' if pc == c else 'B'
        cell1, cell2 = (r, c + 1), (r + 1, c)
        if cell1 in cells and cells[cell1] == '':
            cells[cell1] = cell_type
        if cell2 in cells and cells[cell2] == '':
            cells[cell2] = cell_type
    elif s == '7':
        cell_type = 'A' if pr == r else 'B'
        cell1, cell2 = (r, c + 1), (r - 1, c)
        if cell1 in cells and cells[cell1] == '':
            cells[cell1] = cell_type
        if cell2 in cells and cells[cell2] == '':
            cells[cell2] = cell_type
    elif s == 'F':
        cell_type = 'A' if pc == c else 'B'
        cell1, cell2 = (r, c - 1), (r - 1, c)
        if cell1 in cells and cells[cell1] == '':
            cells[cell1] = cell_type
        if cell2 in cells and cells[cell2] == '':
            cells[cell2] = cell_type


def color(curr):
    r, c = curr
    adj = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
    for a in adj:
        if a in cells and cells[a] == '':
            cells[a] = cells[curr]
            color(a)


def symbol(r, c):
    return maze[r][c]


if __name__ == '__main__':
    sys.setrecursionlimit(10_000)
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
    s_symbol = (row, col)
    cells[s_symbol] = 'S'
    last = [s_symbol, s_symbol]
    d = 1
    path = [s_symbol]
    while current[0] != current[1]:
        for coor in current:
            cells[coor] = 'P'
        path.insert(0, current[1])
        path.append(current[0])
        current, last = [adjacent(current[0], last[0]), adjacent(current[1], last[1])], current
        d += 1
    cells[current[0]] = 'P'
    path.append(current[0])
    last_cell = path[-1]
    for curr_cell in path:
        neighbours(curr_cell, last_cell)
        last_cell = curr_cell
    color_cells = [coor for coor in cells if cells[coor] in ['A', 'B']]
    for coor in color_cells:
        color(coor)
    for row, line in enumerate(maze):
        for col, sym in enumerate(line):
            if cells[row, col] == 'S':
                print(end=f'\033[92m{sym}')
            elif cells[row, col] == 'P':
                print(end=f'\033[93m{sym}')
            elif cells[row, col] == 'A':
                print(end=f'\033[91m{sym}')
            elif cells[row, col] == 'B':
                print(end=f'\033[96m{sym}')
            else:
                print(end=f'\033[90m{sym}')
    print(f'\033[97md={d}, a={list(cells.values()).count('A')}, b={list(cells.values()).count('B')}')
