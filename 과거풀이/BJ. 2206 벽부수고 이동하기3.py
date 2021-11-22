# BJ. 2206 벽부수고 이동하기2
# check 배열 하나 필요하다.
# distance 배열 하나.


# 현재문제. 한개 벽을 부수고 간 거리가 안부수고 간 거리보다 짧기 때문에 안부수고 간거리가 더 나아가지못하고있따.
# 하지만 마지막에 무조건 하나를 부숴야하는데 이래되면 답이 나오지가 않는다.
# 따라서 그걸 알수있는 distance 배열이 하나 더필요하다.
# 더 효율적인 방법은 3차원 배열이긴하다.


from collections import deque

def breaking():

    que = deque()
    que.append([0, 0, -1])  # -1이면 false 1이면 True

    broken_distance = [ [ 0 for _ in range(m)] for _ in range(n) ]
    distance = [ [ 0 for _ in range(m)] for _ in range(n) ]
    distance[0][0] = 1
    broken_distance[0][0] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    while que:
        x, y, status = que.popleft()

        if x == n-1 and y == m-1:
            if status == 1:
                return broken_distance[n-1][m-1]
            else:
                return distance[n-1][m-1]

        for i in range(4):
            row = x + dx[i]
            col = y + dy[i]

            if n > row > -1 and m > col > -1:
                if status == -1:
                    if distance[row][col]:
                        continue
                    if walls[row][col]:
                        broken_distance[row][col] = distance[x][y] + 1
                        que.append([row, col, 1])
                        continue
                    distance[row][col] = distance[x][y] + 1
                    que.append([row, col, -1])

                else:
                    if walls[row][col]:
                        continue
                    if broken_distance[row][col]:
                        continue

                    broken_distance[row][col] = broken_distance[x][y] + 1
                    que.append([row, col, 1])
    return -1


n, m = map(int, input().split())

walls = [ list(map(int, input())) for _ in range(n)]

print(breaking())