# 1244. 최대 상금 문제 풀이 -> 백트래킹(BFS, DFS)
#
# from collections import deque
#
# d = [1, 10, 100, 1000, 10000, 100000]
#
# for tc in range(1, int(input() + 1)):
#     num, cnt = map(str, input().split())
#     N = len(num)
#     cnt = int(cnt)
#     ans = 0
#     visit = [set() for _ in range(cnt + 1)]  # set을쓰면 vist을 초기화시킬필요가없다.?
#     Q = deque()
#     Q.append((int(num), 0))
#     while Q:
#         val, k = Q.popleft()
#         if k == cnt:
#             ans = max(ans, val)
#         else:
#             for i in range(N - 1):
#                 for j in range(i + 1, N):
#                     # i, j 번 위치의 해당하는 값을 추출
#                     a = (val // d[i]) % 10
#                     b = (val // d[j]) % 10
#                     t = val - a*d[i] + b*d[i] - b*d[j] + a*d[j]
#                     if val in visit[k + 1]: continue
#                     visit[k + 1].add(t)
#                     Q.append((t, k + 1 ))
#     print('#{} {}'.format(tc, ans))



visit = [[0] * 1000000 for _ in range(11)]  # 44만개, 44MB  // 밖에 만들었다면 visit을 초기화시켜야한다.
for tc in range(1, int(input()) + 1):
    num, cnt = map(str, input().split())
    N = len(num)
    num = list(map(int, num))
    cnt = int(cnt)
    ans = 0

    def getVal():
        ret = 0
        for v in num:
            ret = ret * 10 + v
        return ret

    def backtrack(k):  # 높이 = 교환횟수
        val = getVal()
        if visit[k][val] == tc: return
        visit[k][val] = tc  # 내가 평소에 하던 것처럼 변화하는 값을 visit에 넣어서 초기화를 안시켜줘도되는것.
        if k == cnt:
            global ans;  # ans하고 비교해서 저장
            ans = max(ans, getVal())
        else:
            for i in range(N - 1):
                for j in range(i + 1, N):
                    num[i], num[j] = num[j], num[i]
                    backtrack(k + 1)
                    num[i], num[j] = num[j], num[i]

    backtrack(0)
    print('#{} {}'.format(tc, ans))