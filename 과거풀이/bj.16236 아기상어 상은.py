# bfs가 최단거리를 찾는거니깐 한번 찾았으면 더이상 탐색을 안한다?
# 그래도 되나?

from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n = int(input())
sea = []
for i in range(n):
    inp = list(map(int, input().split()))
    sea.append([])
    for j in range(n):
        if inp[j] == 9:
            sx, sy = j, i
            sea[i].append(0)
        else:
            sea[i].append(inp[j])
size = 2
rewind = time = feed = 0

finish = False

while not finish:
    Q = deque()
    Q.append((sx, sy))
    visit = [[0 for _ in range(n)] for _ in range(n)]
    visit[sy][sx] = 1
    lst = []
    is_find = False
    while Q and not is_find:  # and니깐 둘다 참이어야 돌아가는거아닌가?
        for i in range(len(Q)):
            x, y = Q.popleft()
            for dir in range(4):
                tx = x + dx[dir]
                ty = y + dy[dir]
                if -1 < tx < n and -1 < ty < n and not visit[ty][tx] and sea[ty][tx] <= size:
                    if sea[ty][tx] == size or not sea[ty][tx]:
                        Q.append((tx, ty))
                    elif sea[ty][tx]:
                        is_find = True
                        lst.append((tx, ty))
                    visit[ty][tx] = 1
        time += 1
    if not is_find:
        finish = True
    else:
        if len(lst) > 1:
            lst.sort(key=lambda x: [x[1], x[0]])
        sx, sy = lst[0][0], lst[0][1]
        sea[sy][sx] = 0
        feed += 1
        if feed == size:
            size += 1
            feed = 0
        rewind = time
print(rewind)

