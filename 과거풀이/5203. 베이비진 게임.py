# 5203. 베이비진 게임

def babyjin(p):
    temp = list(set(p))
    for k in range(len(p)-2):
        if p[k] == p[k+1] == p[k+2]:
            return 1

    if len(temp) >= 3:
        for k in range(len(temp)-2):
            if temp[k] == temp[k+1] - 1 == temp[k+2] - 2:
                return 1

    return 0


T = int(input())

for tc in range(T):

    p1 = []
    p2 = []
    cards = list(map(int, input().split()))
    for j in range(12):
        i = cards[j]
        if j & 1:
            p2.append(i)
            if len(p2) >= 3:
                p2.sort()
                if babyjin(p2):
                    print('#{}'.format(tc+1), 2)
                    break
        else:
            p1.append(i)
            if len(p1) >= 3:
                p1.sort()
                if babyjin(p1):
                    print('#{}'.format(tc+1), 1)
                    break
    else:
        print('#{}'.format(tc+1), 0)
