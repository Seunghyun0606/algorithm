# 이분탐색으로 풀어야한다.

n, m = map(int, input().split())

trees = list(map(int, input().split()))

l, r = 1, max(trees)

while l <= r:
    
    mid = (l+r) // 2

    sliced_log = 0
    for tree in trees:
        if tree > mid:
            sliced_log += tree - mid
    
    if sliced_log >= m:
        l = mid + 1
    else:
        r = mid - 1
print(r)
