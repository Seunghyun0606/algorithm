# 스택, 큐
# i 번 트럭이 지나간길이 == 다리 길이면 다리를 지난 트럭으로 넣어준다.
# 시간은 따로 흐르는 중
# 다리를 건너는 트럭 ( trucck_wights )가 빈배열이 되면 끝낸다.
# 단, 다리 하중이 버틸 수 없을때는 시간만지나간다.

from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    
    bridge = deque([0]*bridge_length)
    truck = deque(truck_weights)
    my_sum = 0
    while bridge:
        time += 1
        last = bridge.popleft()
        my_sum -= last
        if truck:
            my_sum += truck[0]
            if weight >= my_sum:
                bridge.append(truck.popleft())
            else:
                my_sum -= truck[0]
                bridge.append(0)

    return time