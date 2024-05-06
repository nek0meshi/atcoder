# coding: utf-8

BLACK = '#'
WHITE = '.'

def isCenterOfDonut(x, y, data):
    # print(['x,y', x, y, data[y][x]])
    if data[y][x] == BLACK:
        return False

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue

            # print(['i,j', i, j, x + i, y + j, data[y + j][x + i]])

            if data[y + j][x + i] == WHITE:
                return False

    return True

def countDonut(width, height, data):
    count = 0

    for x in range(1, width - 1):
        for y in range(1, height - 1):
            if isCenterOfDonut(x, y, data):
                count += 1

    return count

def execTest(height, width, rows):
    # string[][]
    # strin[j][i] ... j行目・i列目の文字列(# or .)
    data = [list(row) for row in rows]

    print(countDonut(width, height, data))

def main():
    height, width = map(int, input().split())

    rows = [input() for i in range(height)]

    execTest(height, width, rows)

main()
