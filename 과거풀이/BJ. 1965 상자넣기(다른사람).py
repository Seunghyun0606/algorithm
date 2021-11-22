import sys
read = sys.stdin.readline

# 하나씩 Queue에 넣어서 수열에서 꺼낸 값이 queue에 있는 값보다 작으면 교체해주면서
# 작은 값들을 하나씩 늘려나가는 방식이다. 이걸로 최장거리 구할수있겠는데?
# 심지어 LCS는 238ms 이건 100ms로 2배 빠른데 메모리는 같다.

int(read())
queue = []
q_len = 0
for i in map(int, read().split()):
    check = True
    for j in range(q_len):
        if queue[j] >= i:
            queue[j] = i
            check = False
            break
    if check:
        queue.append(i)
        q_len += 1

print(q_len)
