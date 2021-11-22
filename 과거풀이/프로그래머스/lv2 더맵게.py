# heapq는 우선순위 큐이다.
# 알아서 넣고 빼면서 정렬이되고, 노드의 제일 위에있는게 제일 작다

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) > 1:
        first = heapq.heappop(scoville)
        if first >= K:
            return answer
        
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second*2)
        answer += 1
    else:
        # 1, 2 ,3 11 의 경우, 만약 딱 1개 남았을때 끝나면 return answer <-- 이게 못걸리기때문이다.
        if scoville[0] >= K:
            return answer
        return -1