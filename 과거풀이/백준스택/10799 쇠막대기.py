# 스택 문제, 레이져로 쇠막대기를 자른다. () 는 무조건 레이져
# ( < 막대기 시작 ) < 막대기 끝
# 막대기 갯수는 여는 괄호 갯수. 층 수 -> len(stack)

raser = list(input())
stack = []
result = 0
for i in range(len(raser)):
    if raser[i] == '(':
        stack.append(raser[i])
    
    else:
        if raser[i-1] == '(':   
            # 층수, 즉 앞에 쌓인 ((( 갯수
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1
            # 끝날때 맨위에 층 -> 왜냐면 다음꺼에서 쇠막대기가 쪼개지거나 층이 나뉘면, 그 다음 층수 쌓인거에서 나머지 밑에꺼를 계산함
            # 나중에 그림보면 이해가능

print(result)