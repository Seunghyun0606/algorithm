# BJ. 1965 상자넣기
# dp문제이긴한데 체크배열만들어서 해도될거같은데?
# 응 안되, LCS 써야해.


def lcs(idx, start, target, cnt):  # target = boxes[0] start = 0, cnt = 1
    if start == n-1:
        dp[idx] = max(dp[idx], cnt)
        return
    for i in range(start+1, n):
        if boxes[i] > boxes[idx]:
            dp[i] = -1
        if boxes[i] > target:
            temp_target = target
            target = boxes[i]
            lcs(idx, i, target, cnt+1)
            target = temp_target
    dp[idx] = max(dp[idx], cnt)
    return


n = int(input())

boxes = list(map(int, input().split()))
dp = [ 0 for _ in range(n) ]

for k in range(n):
    if dp[k]:
        continue
    lcs(k, k, boxes[k], 1)

print(max(dp))
