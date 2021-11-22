# BJ. 2573 빙산5 (BFS시간단축)
# ?? readline 쓰면 오히려 4560 -> 4668ms 느려짐.
# 이 코드는 다른 사람 코드.
# 함수안에 넣고, cnt로 했음.


from sys import stdin
from _collections import deque
input = stdin.readline

n, m = [int(x) for x in input().rstrip().split()]
arr = []
cnt = 0
for _ in range(n):
    arr.append([int(x) for x in input().rstrip().split()])
    for j in arr[-1]:
        if j:
            cnt += 1
new_cnt = cnt


def bfs(i, j):
    global new_cnt
    visited = {(i, j)}
    queue = deque([(i, j)])
    while queue:
        i, j = queue.popleft()
        for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            if not (0 <= i+di < n and 0 <= j+dj < m):
                continue
            if not arr[i + di][j + dj] and (i+di, j+dj) not in visited:
                if arr[i][j]:
                    arr[i][j] -= 1
                    if not arr[i][j]:
                        new_cnt -= 1
            elif (i+di, j+dj) not in visited:
                visited.add((i+di, j+dj))
                queue.append((i+di, j+dj))
    return len(visited)


def run():
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                if cnt != bfs(i, j):
                    return True
                return False
    else:
        print(0)
        exit()


time = 0
while not run():
    cnt = new_cnt
    time += 1
print(time)

