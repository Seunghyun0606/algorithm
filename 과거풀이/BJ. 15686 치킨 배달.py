# BJ. 15686 치킨 배달

# 최대 m개 이니깐 m 까지 depth 만들고 그때의 부분집합을 만들자
# 단, 000은안됨. 무조건 1개의 치킨집은 있어야한다.
# 이때의 치킨거리 최솟값은 2와 1사이의 거리 count 하면된다.
# 치킨집 총 갯수 C m (조합)


def distance_calc(chic):

    distance = 0
    chicken1 = []
    for i in range(1, len(chic)):
        if chic[i]:
            chicken1.append(chicken[i-1])

    for i in house:
        temp1 = []
        for j in chicken1:
            temp1.append(abs(i[0] - j[0]) + abs(i[1] - j[1]))
        distance += min(temp1)

    return distance


def combi(depth, idx):
    visit[idx] = 1

    if depth < m+1:  # 사실상 문제의 의도는 m일때만 고려하면된다. subset으로도 푸는 방법이있긴하다.(다만 조금 느림 해인이꺼 참조.)
        if depth > 0:
            global distance_min
            temp = distance_calc(visit)
            if distance_min > temp:
                distance_min = temp

        for i in range(idx+1, len(chicken)+1):
            if visit[i]:
                continue
            combi(depth+1, i)
            visit[i] = 0


n, m = map(int, input().split())

city = [ [] for _ in range(n) ]
house = []
chicken = []

for i in range(n):
    for j, value in enumerate(list(map(int, input().split()))):
        city[i].append(value)
        if value == 1:
            house.append([i, j])  # house의 위치 행, 열 값.
        elif value == 2:
            chicken.append([i, j])

visit = [0] * (len(chicken)+1)

distance_min = 10 ** 5

combi(0, 0)

print(distance_min)

