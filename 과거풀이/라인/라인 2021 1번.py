# 딕셔너리에 넣자.
# 2의 배수만큼 있으면 넣자.
# 갯수는 초기 리스트 갯수

from collections import defaultdict

def solution(boxes):
    answer = -1

    len_boxes = len(boxes)
    items = defaultdict(int)

    for box in boxes:
        for item in box:
            items[item] += 1
    
    new_items = list(items.values())

    count = 0
    for item in new_items:
        temp = item // 2
        if temp:
            count += temp
    
    if len_boxes > count:
        answer = len_boxes - count
    else:
        answer = 0
    
    return answer


