# BFS

from collections import deque

def exit(r, c):
    forest = []

    start_place = deque()
    end_place = []
    waters = deque()

    for i in range(r):
        temp = []
        check_row = input()
        for j in range(c):
            
            if check_row[j] == 'S':
                start_place.append((i, j, 0))
            elif check_row[j] == 'D':
                end_place = [i, j]
            elif check_row[j] == '*':
                waters.append((i, j))

            temp.append(check_row[j])
        forest.append(temp)

    x = [1, -1, 0, 0]
    y = [0, 0, 1, -1]

    forest[start_place[0][0]][start_place[0][1]] = 1

    while waters or start_place:
        temp1 = []
        temp2 = []
        while waters:
            r1, c1 = waters.popleft()
            for i in range(4):
                row = r1 + x[i]
                col = c1 + y[i]

                if r > row > -1 and c > col > -1 and forest[row][col] != 'X' and forest[row][col] != '*' and forest[row][col] != 'D':
                    forest[row][col] = '*'
                    temp1.append((row, col))
        while start_place:
            r1, c1, d = start_place.popleft()
            for i in range(4):
                row = r1 + x[i]
                col = c1 + y[i]

                if r > row > -1 and c > col > -1 and forest[row][col] != 'X' and forest[row][col] != '*' and forest[row][col] != 1:
                    if forest[row][col] == 'D':
                        print(d+1)
                        return
                    forest[row][col] = 1
                    temp2.append((row, col, d+1))
        for temp in temp1:
            waters.append(temp)
        for temp in temp2:
            start_place.append(temp)
    print('KAKTUS')

r, c = map(int, input().split())

exit(r, c)
