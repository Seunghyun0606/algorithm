
# 입력: 블로그 시작한지 N일 / 누적방문일 수 X일
# 출력: X일 동안 들어온 누적 방문자 수와 기간

# dp로 풀어야함. 아니면 시간초과뜸

import sys
input = sys.stdin.readline

n, x = map(int, input().split())

entered_people_num = list(map(int, input().split()))

first_accum = sum(entered_people_num[:x])

max_people_num = first_accum
how_many = 1
accum_dp = [first_accum]

for i in range(n-x):
    # 최대, 최소 빼면 next accum
    next_accum = accum_dp[i] - entered_people_num[i] + entered_people_num[i+x]
    accum_dp.append(next_accum)

    if next_accum > max_people_num:
        max_people_num = next_accum
        how_many = 1
    elif next_accum == max_people_num:
        how_many += 1

if max_people_num:
    print(max_people_num)
    print(how_many)
else:
    print("SAD")





# 시간초과뜸
# import sys
# input = sys.stdin.readline

# n, x = map(int, input().split())

# entered_people_num = list(map(int, input().split()))

# max_people_num = 0
# how_many = 0

# indexing = 0

# while indexing < n:
#     accum = sum(entered_people_num[indexing:indexing + x])
#     if accum > max_people_num:
#         max_people_num = accum
#         how_many = 1
#     elif accum == max_people_num:
#         how_many += 1
    
#     indexing += 1

# if max_people_num:
#     print(max_people_num)
#     print(how_many)
# else:
#     print("SAD")



