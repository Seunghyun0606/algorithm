# 처음에 col 고려하다가, 안고려해도 되는줄  알았는데, 결국 고려해야만 풀수있었다.

def solution(numbers, hand):
    answer = ''

    if len(hand) > 4:
        hand = "R"
    else:
        hand = "L"

    left_set = [1, 4, 7]  # 열이 0
    right_set = [3, 6, 9]  # 열이 2
    # mid_set = 2 5 8 0 열은 1 행은

    sl_row, sl_col = 3, 0
    sr_row, sr_col = 3, 2

    for num in numbers:
        if num in left_set:
            sl_row = num // 3
            sl_col = 0
            answer += 'L'
        elif num in right_set:
            sr_row = (num // 3) - 1
            sr_col = 2
            answer += 'R'
        else:
            col = 1
            if num:
                row = num // 3
            else:
                row = 3

            left = abs(row - sl_row) + abs(col - sl_col)
            right = abs(row - sr_row) + abs(col - sr_col)

            if left == right:
                if hand == "R":
                    sr_row = row
                    sr_col = 1
                else:
                    sl_row = row
                    sl_col = 1
                answer += hand
            elif left > right:
                sr_row = row
                sr_col = 1
                answer += "R"
            else:
                sl_row = row
                sl_col = 1
                answer += "L"

    return answer