import sys
sys.stdin = open('cheese.txt', 'r')
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
field = []
visit_A = [[0]*M for _ in range(N)]
visit_B = [[0]*M for _ in range(N)]

cnt = area = 0
px = py = 0
tmpx = tmpy = 0

for i in range(N):
    arr = [int(x) for x in input().split()]
    field.append(arr)

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def DFS_Air(x, y):
    global px
    global py

    visit_A[x][y] = 1

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]

        if tx < 0 or ty < 0 or tx >= N or ty >= M:
            continue
        if visit_A[tx][ty] == 1 or field[tx][ty] == -1:
            continue
        if field[tx][ty] == 1:
            field[tx][ty] = -1
            px = tx
            py = ty
            continue
        DFS_Air(tx, ty)

def DFS_Melt(x, y):
    global area

    visit_B[x][y] = 1
    field[x][y] = 0

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]

        if tx < 0 or ty < 0 or tx >= N or ty >= M:
            continue
        if visit_B[tx][ty] == 1 or field[tx][ty] == 1:
            continue
        if field[tx][ty] == -1:
            area += 1
        DFS_Melt(tx, ty)

for i in range(N):
    for j in range(M):
        if visit_A[i][j] == 0 and field[i][j] == 0:
            visit_A = [[0]*M for _ in range(N)]
            DFS_Air(i, j)
            if (tmpx, tmpy) != (px, py):
                visit_B = [[0]*M for _ in range(N)]
                area = 1
                DFS_Melt(px, py)
                cnt += 1
                tmpx = px
                tmpy = py

print(cnt)
print(area)