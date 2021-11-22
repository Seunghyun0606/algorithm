# 인형뽑기, 각 리스트를 스택이라 생각하고, 인형모으는 상자도 스택으로 생각한다
# 뽑을때 스택이 비어있는거만 주의하면 될듯하다.

# 방법이 두가지다.
# 방법1. 전처리로 1. 회전, 2. 0을 모두제거, 스택형식으로 하나씩 빼는 방법
# 방법2. 그냥 귀찮지만, 0을 하나하나 판단하면서 파고들어가는거지 뭐
# 일단 방법2로 먼저해보고 1도 해보자

def solution(board, moves):
    answer = 0

    my_board = board
    n = len(my_board)
    my_stack = []

    for c in moves:
        c -= 1
        for r in range(n):
            doll = my_board[r][c]
            if doll:
                if my_stack:
                    doll_check = my_stack[-1]
                    if doll_check == doll:
                        my_stack.pop()
                        print(doll)
                        answer += 2
                    else:
                        my_stack.append(doll)
                else:
                    my_stack.append(doll)

                my_board[r][c] = 0
                break
    return answer