# BJ.1911 흙길 보수하기
# N은 물웅덩이 L은 널빤지 길이 // 널빤지 최소 갯수


N, L = map(int, input().split())


panels = []
checkLen = 0

for i in range(N):
    temp = []
    for j in map(int, input().split()):
        temp.append(j)
    panels.append(temp)
    if checkLen < temp[1]:
        checkLen = temp[1]

panels.sort()

check = [0] * (checkLen + 1)
cnt = 0

for i in panels:
    s, e = i
    while s < e:
        if not check[s]:
            for j in range(L):
                if s+j > len(check)-1:
                    break
                check[s+j] = 1
            s += L
            cnt += 1
        else:
            s += 1

print(cnt)



