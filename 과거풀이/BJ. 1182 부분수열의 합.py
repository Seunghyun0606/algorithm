# BJ. 1182 부분수열의 합


def subsequence(start, end):
    global count

    if start == end:
        if 1 in sub:
            temp = 0
            for i in range(n):
                if sub[i]:
                    temp += nums[i]
            if temp == s:
                count += 1

    else:
        for j in range(2):
            sub[start] = j
            subsequence(start+1, end)


n, s = map(int, input().split())

nums = list(map(int, input().split()))

sub = [0]*n
count = 0
subsequence(0, n)
print(count)