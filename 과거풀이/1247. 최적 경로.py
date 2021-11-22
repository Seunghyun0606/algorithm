# 1247. 최적 경로

def DFS(depth, x, y, ans):

    if depth == n:
        global result
        ans += abs(x-where[1][0]) + abs(y-where[1][1])
        result = min(result, ans)
        return
    if ans > result:
        return

    for i in range(2, n+2):
        if visit[i]:
            continue
        x1, y1 = where[i]
        visit[i] = 1
        DFS(depth+1, x1, y1, ans + abs(x1-x) + abs(y1-y))
        visit[i] = 0


T = int(input())

for tc in range(T):

    n = int(input())
    where = []

    temp = []
    for i in map(int, input().split()):
        if len(temp) == 2:
            where.append(temp)
            temp = []
        temp.append(i)
    where.append(temp)
    result = 987654321

    visit = [0] * (n+2)

    DFS(0, where[0][0], where[0][1], 0)

    print('#{}'.format(tc+1), result)
