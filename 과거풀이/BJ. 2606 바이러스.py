# BJ. 2606 바이러스
# 1번 컴퓨터는 제외.


def virus(start):
    global count
    visit[start] = 1
    count += 1
    for j in dot[start]:
        if visit[j]:
            continue
        virus(j)
    


n = int(input())
edge = int(input())

dot = [ [] for _ in range(n+1) ]
visit = [0] * (n+1)
count = -1
for i in range(edge):
    a, b = map(int, input().split())
    dot[a].append(b)
    dot[b].append(a)

virus(1)
print(count)


