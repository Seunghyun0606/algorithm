from collections import deque
T = int(input())

for _ in range(T):
    n, m = map(int, input().split())

    que = deque(map(lambda x: [int(x), 0], input().split()))
    que[m] = [que[m][0], 1]
    cnt = 0
    while que:
        value, check = que.popleft()
        for i in range(len(que)):
            if que[i][0] > value:
                que.append([value, check])
                break
        else:
            cnt += 1
            if check:
                print(cnt)
                break
