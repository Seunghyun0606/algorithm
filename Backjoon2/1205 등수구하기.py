# 총 리스트 점수 개수 N
# 랭킹리스트 점수 개수 P
# 만약, 랭킹 리스트가 꽉 차있을 때, 새 점수가 이전 점수보다 더 좋을 때만 점수가 바뀐다.

from collections import deque

N, my_record, P = map(int, input().split())

# 몇등하는지 출력해야한다.
# 랭킹 리스트가 꽉 차있을 때, 새 점수가 이전 점수보다 더 좋을 때만 점수가 바뀐다.
if N:
    rank_list = list(map(int, input().split()))

    que = deque(rank_list)
    for _ in range(P-N):
        que.append(-1)

    # queue 에서 맨 앞에 점수 하나씩 꺼내면서 P 이하인지 count센다
    # P를 넘지않으면서 점수가 높은게 나오면 해당 랭크에 들어갈수있다.
    cnt = 0
    flag = 0
    while que:
        cnt += 1
        max_record = que.popleft()
        if my_record > max_record:
            flag = 1
            break
        elif N == P and rank_list[-1] >= my_record:
            flag = 0
            break
        elif my_record == max_record and N < P:
            flag = 1
            break
        elif my_record == max_record and que:
            
            if {my_record} - set(que):
                flag = 1
            else:
                flag = 0
            break
    if flag:
        print(cnt)
    else:
        print(-1)


# 총리스트가 비어있으므로, 무조건 1등
else:
    print(1)

# 다른사람풀이
# n, Eugene, p = map(int, input().split())

# if n == 0:
#     print(1)
# else:
#     ranking = list(map(int, input().split()))
#     if n == p and ranking[-1] >= Eugene:
#         print(-1)
#     else:
#         rank = n + 1
#         for i in range(n):
#             if ranking[i] <= Eugene:
#                 rank = i + 1
#                 break
#         print(rank)