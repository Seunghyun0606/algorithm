# 실패 나중에 풀어보자.

n = int(input())

papers = [ list(map(int, input().split())) for _ in range(n) ]
result = [0, 0]
def divide(row, col, n):

    if n == 1:
        if papers[row][col]:
            return 1
        else:
            return 0
    else:
        a = divide(row, col, n//2)
        b = divide(row + n//2, col, n//2)
        c = divide(row, col + n//2, n//2)
        d = divide(row + n//2, col + n//2, n//2)
        temp = a+b+c+d
        if temp == n**2:
            return temp
        else:
            # 0이 흰색종이, 1이 파란색종이
            # 칸이 1개이거나 2개이다.
            if n == 2:
                result[0] += 4 - temp
                result[1] += temp
            else:
                if temp == (n//2)**2:
                    result[0] += 3
                    result[1] += 1
                else:
                    result[0] += 2
                    result[1] += 2
            return 0

divide(0, 0, n)
print(*result, sep='\n')


# def divide(row, col, n):

#     if n == 1:
#         if papers[row][col]:
#             result[0] += 1
#         else:
#             result[1] += 1
#     else:
#         divide(row, col, n//2)
#         divide(row + n//2, col, n//2)
#         divide(row, col + n//2, n//2)
#         divide(row + n//2, col + n//2, n//2)

# divide(0, 0, n)
# print(*result, sep='\n')