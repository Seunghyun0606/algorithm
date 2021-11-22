def solution(n, arr1, arr2):
    answer = []
    secret_map = [ [0]*n for _ in range(n) ]
    def get_map(arr):
        for i in range(n):
            temp = []
            a = arr[i]
            while a:
                if a % 2:
                    temp.append(1)
                else:
                    temp.append(0)
                a = a // 2
            else:
                temp += [0]*(n-len(temp))
            for j in range(n):
                if temp[n-1-j]:
                    secret_map[i][j] = '#'
                else:
                    if secret_map[i][j] == '#':
                        continue
                    secret_map[i][j] = ' '
    get_map(arr1)
    get_map(arr2)

    for k in range(n):
        secret_map[k] = ''.join(secret_map[k])
    return secret_map