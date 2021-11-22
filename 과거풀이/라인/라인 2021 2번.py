# deque에 넣어서 앞뒤로 빼자.
# 빠져나온 건 딕셔너리에 넣자 (검색효율 때매)
# 기존 리스트에서 맨 앞이랑 맨 뒤 검색하고, 딕셔너리에 없으면 기존 오더대로 빼자

from collections import deque


def solution(ball, order):
    answer = []

    wait_orders = deque()
    new_ball = deque(ball)

    while len(answer) < len(ball):
        for order_num in order:
            if new_ball:  # ball이 남아있냐?
                # 보류값 먼저 검사(우선순위)
                cnt = 0
                while len(wait_orders) > cnt:
                    front = new_ball[0]
                    back = new_ball[-1]

                    wait_order = wait_orders.popleft()
                    if wait_order == front:
                        answer.append(new_ball.popleft())
                        cnt = 0
                        # wait_orders.popleft()
                        continue
                    elif wait_order == back:
                        answer.append(new_ball.pop())
                        cnt = 0
                        # wait_orders.popleft()
                        continue
                    else:
                        wait_orders.append(wait_order)
                    cnt += 1

                if order_num == new_ball[0]:    # 맨 앞이냐?
                    answer.append(new_ball.popleft())
                elif order_num == new_ball[-1]: # 맨 뒤냐?
                    answer.append(new_ball.pop())
                else:                     # 둘다 아니냐?
                    # 둘다 아니면, 해당 값이 보류 값에 있는지 확인하고 없으면 보류해둔다.
                    wait_orders.append(order_num)

    return answer

# solution([11, 2, 9, 13, 24], [9, 2, 13, 24, 11])

# # a = {1: 1, 2: 2}
# # b = {}
# # c = dict()
# # if c:
# #     print(1)