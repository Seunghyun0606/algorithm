import sys
input = sys.stdin.readline

n, m = map(int, input().split())
times = [ int(input()) for _ in range(n)]
left = 0
right = max(times) * m
answer = 0
while right >= left:
    mid = ( right + left ) // 2

    how_many_people = 0

    for time in times:
        how_many_people += mid // time

        if how_many_people > m:
            break
    if how_many_people >= m:
        right = mid - 1
        answer = mid
    else:
        left = mid + 1
print(answer)