# 3349. 최솟값으로 이동하기
# 출발점 x y가 도착점 x y보다 둘다 크거나 작을때 // 하나만 크고 작을때.

T = int(input())

for tc in range(T):

    w, h, n = map(int, input().split())

    places = [ list(map(int, input().split())) for _ in range(n) ]

    count = 0
    for i in range(n-1):
        a, b = places[i][0], places[i][1]
        a1, b1 = places[i+1][0], places[i+1][1]

        if a > a1 and b < b1:
            count += (a-a1) + (b1-b)
        elif a < a1 and b > b1:
            count += (b-b1) + (a1-a)

        elif a == a1 and (b > b1 or b < b1):
            count += abs(b-b1)

        elif b == b1 and (a > a1 or a < a1):
            count += abs(a-a1)

        elif a > a1 and b > b1:
            c = a-a1
            d = b-b1
            if c > d:
                count += d + (c-d)
            else:
                count += c + (d-c)

        else:
            c = a1-a
            d = b1-b
            if c > d:
                count += d + (c-d)
            else:
                count += c + (d-c)

    print('#{}'.format(tc+1), count)


