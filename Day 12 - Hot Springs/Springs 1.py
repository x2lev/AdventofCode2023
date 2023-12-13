import re

with open('test', 'r') as f:
    springs = [(match.group(1), [int(x) for x in match.group(2).split(',')])
               for match in re.finditer(r'([.?#]+) ([\d,]*)', f.read())]

if __name__ == '__main__':
    possibilities = 0
    for row, groups in springs:
        print(row)
        for chunk in re.finditer(r'(?=[.?#])+', row):
            print(chunk)
