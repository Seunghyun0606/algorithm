# 3752. 가능한 시험 점수


def calc_score(depth, temp):

    if depth == n:
        return

    else:
        for i in range(0, n):
            if check[temp]:
                continue
            else:
                check[temp] = 1
                result.append(temp)
            calc_score(depth+1, temp + scores[i])


T = int(input())

for tc in range(T):
    n = int(input())
    scores = list(map(int, input().split()))

    check = [0] * (sum(scores)+1)
    result = []
    calc_score(0, 0)
    print(result)
    print(check)
    print('#{}'.format(tc+1), len(result))


