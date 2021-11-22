# # 10888. 음식배달 D4
# # 조합으로 음식점 갯수 뽑아내고, 각 음식점 갯수에 맞는 최단거리뽑기


T = int(input())

for t in range(T):
    n = int(input())

    food_chain = []
    deliver_map = []
    homes = []

    for i in range(n):
        temp = []
        temp2 = map(int, input().split())
        for j, k in enumerate(temp2):
            if k > 1:
                food_chain.append([i, j])
            elif k == 1:
                homes.append([i, j])
            temp.append(k)
        deliver_map.append(temp)

    min_dist = 10**6

    comb_check = [0]*len(food_chain)
    def comb(k):
        if k == len(food_chain):
            # 거리찾기 함수
            find_dist()
            return
        else:
            for i in range(2):
                comb_check[k] = i
                comb(k+1)

    def find_dist():
        global min_dist
        dist_map = [ [ 9999 for _ in range(n) ] for _ in range(n) ]
        value = 0
        for j in range(len(comb_check)):
            if comb_check[j]:
                fr, fc = food_chain[j]
                value += deliver_map[fr][fc]

                for home in homes:
                    hr, hc = home

                    dist = abs(fr-hr) + abs(fc-hc)

                    if dist < dist_map[hr][hc]:
                        dist_map[hr][hc] = dist
        dist_sum = 0
        for i in range(n):
            for j in range(n):
                if dist_map[i][j] != 9999:
                    dist_sum += dist_map[i][j]
        last = value + dist_sum
        if last:
            min_dist = min(min_dist, last)

    comb(0)
    print('#{} {}'.format(t+1, min_dist))
