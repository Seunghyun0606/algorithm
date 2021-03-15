# 이분탐색.
# 가장 인접한 두 공유기 사이의 거리를 최대한으로 한다.
# 그니깐 인접한 두 공유기 사이의거리를 최대한 유지하며 공유기를 다 설치해야한다.

def check_router(distance):

    installed_place = house[0]
    # router가 이미 맨 첫 자리에 설치되었다고 보는 것.
    count_router = 1

    for i in range(1, n):
        if installed_place + distance <= house[i]:
            installed_place = house[i]
            count_router += 1
    return count_router


n, n_router = map(int, input().split())

house = [ int(input()) for _ in range(n) ]

house.sort()

min_distance = house[1] - house[0]
max_distance = house[-1] - house[0]

left = min_distance
right = max_distance
result = 0

while left <= right:
    mid = ( left + right ) // 2

    if check_router(mid) >= n_router:
        left = mid + 1
        result = mid
    else:
        right = mid - 1

print(result)