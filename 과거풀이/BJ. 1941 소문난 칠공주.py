# BJ. 1941 소문난 칠공주 // 실패


def s_team(depth, x, y, cnt):
    visit[x][y] = 1

    if depth > 3 and cnt == -4:  # Y가 4개 나오면 무조건 안됨.
        return

    if depth == 7:
        if cnt > 0:
            global count
            count += 1
            print(visit)
        return

    else:
        for i in range(4):
            row = x + dx[i]
            col = y + dy[i]
            if 5 > row > -1 and 5 > col > -1:
                if visit[row][col]:
                    continue
                if students[row][col] == 'S':
                    s_team(depth+1, row, col, cnt+1)
                else:
                    s_team(depth+1, row, col, cnt-1)
                visit[row][col] = 0


students = [ list(input()) for _ in range(5)]
visit = [ [0 for _ in range(5)] for _ in range(5)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
count = 0

for i in range(5):
    for j in range(5):
        if students[i][j] == 'S':
            s_team(1, i, j, 1)

print(count)

