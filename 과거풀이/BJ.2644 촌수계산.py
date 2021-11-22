# BJ.2644 촌수계산


from collections import deque


def find_relations(target1, time):
    que = deque()
    que.append([target1, time])
    while que:
        r1, time1 = que.popleft()
        if r1 == target2:
            return time1
        check[r1] = 1
        for i in relations[r1]:
            if check[i]:
                continue
            que.append([i, time1+1])
    return -1


n = int(input())  # 사람 수
target1, target2 = map(int, input().split())

nodes = int(input())

check = [0]*(n+1)  # 1~n까지 0빼고

relations = [0] + [ [] for _ in range(n) ]

for _ in range(nodes):
    t1, t2 = map(int, input().split())
    relations[t1].append(t2)
    relations[t2].append(t1)


print(find_relations(target1, 0))











