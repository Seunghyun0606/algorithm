# BJ. 2573 빙산4 (BFS) 성공.


from collections import deque


def breaking(x1, y1, removing1):
    que = deque()
    que.append([x1, y1])
    iceberg[x1][y1] = removing1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while que:

        x, y = que.popleft()
        temp = 0  # 이것 만큼 copy에서 녹일거임.

        for i in range(4):
            row = x + dx[i]
            col = y + dy[i]

            if n > row > -1 and m > col > -1:
                if iceberg[row][col] == removing1:
                    continue
                elif iceberg[row][col] > 0:
                    iceberg[row][col] = removing1
                    que.append([row, col])
                else:
                    temp += 1
        temp_val = copy[x][y] - temp
        if temp_val < 0:
            check[x][y] = 0
            copy[x][y] = 0
        else:
            check[x][y] = temp_val
            copy[x][y] = temp_val


n, m = map(int, input().split())


iceberg = [ list(map(int, input().split())) for _ in range(n) ]
copy = [[iceberg[i][j] for j in range(m)] for i in range(n)]
check = [[0]*m for _ in range(n)]
removing = 0  # check용
flag2 = False

while True:
    count = 0
    removing -= 1
    flag = True
    for i in range(1, n-1):
        for j in range(1, m-1):
            if iceberg[i][j] > 0:
                breaking(i, j, removing)
                count += 1
                flag = False
                if count == 2:
                    print((removing+1)*(-1))
                    flag2 = True
                    break
        if flag2:
            break
    if flag2:
        break

    if flag:  # 끝까지 안 나눠지는 경우
        print(0)
        break

    iceberg, check = check, iceberg


