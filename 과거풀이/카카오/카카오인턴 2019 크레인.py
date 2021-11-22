# 시작할때 출력값을 자동으로 넣어주는 main이 있나보다.
# board가 순서대로 들어오고, 다음이 moves가 들어온다.
# [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]


def solution(board, moves):

    length = len(board)
    basket = []
    answer = 0

    for i in moves:
        for j in range(length):
            if board[j][i-1]:
                k = board[j][i-1]
                board[j][i-1] = 0
                if basket:
                    if basket[-1] == k:
                        basket.pop()
                        answer += 2
                        break
                    basket.append(k)
                else:
                    basket.append(k)
                break
    return answer



# [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
# [1, 5, 3, 5, 1, 2, 1, 4]