# 가로, 세로, 대각선으로 이어져있으면 같은 섬이다.
# 섬의 개수를 구하는 BFS

from collections import deque

# 좌표
r = [0, 0, 1, -1, 1, 1, -1, -1]
c = [1, -1, 0, 0, 1, -1, 1, -1]


while True:
    n, m = map(int, input().split())
    if not n or not m:
        break
    
    territory = [ list(map(int, input().split())) for _ in range(m) ]

    # 영해에 존재하는 섬 갯수
    count = 0

    # 0이면 바다, 1이면 땅, 2면 이미 지나간 땅
    for i in range(m):
        for j in range(n):
            if territory[i][j] == 1:
                que = deque()
                que.append((i, j))

                while que:
                    row, col = que.popleft()

                    for k in range(8):
                        new_row = row + r[k]
                        new_col = col + c[k]

                        if m > new_row > -1 and n > new_col > -1 and territory[new_row][new_col] == 1:
                            territory[new_row][new_col] = 2
                            que.append( (new_row, new_col) )
                    
                count += 1
    print(count)