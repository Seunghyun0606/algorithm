# 5207. 이진탐색

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    n_list = sorted(list(map(int,input().split())))
    m_list = list(map(int, input().split()))

    cnt = 0
    for num in m_list:
        start = 0
        end = n-1

        flag = 0
        while start <= end:
            mid = (start + end) // 2

            if num >= n_list[mid]:
                if num == n_list[mid]:
                    cnt += 1
                    break

                start = mid + 1
                if flag == 1:
                    break
                flag = 1

            elif num < n_list[mid]:
                end = mid - 1
                if flag == -1:
                    break
                flag = -1

    print('#{}'.format(tc+1), cnt)