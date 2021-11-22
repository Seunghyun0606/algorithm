# 어차피 for문이 좌측에서 우측으로 가니깐, 좌측먼저 확인하고, 있으면 가져오고 없으면 우측꺼 확인하고 가져온다.
# reserve랑 lost로 전처리 리스트를 만든다.
# 2개면 2, 없으면 0

def solution(n, lost, reserve):
    answer = 0
    
    check = [1]*(n+2)  # 모두있는걸로 만들고, 2인거만 찾자. 2개추가한 이유는 양 끝 때문. 마지막에 모두 더한뒤 2 빼면됨

    for cloth in reserve:
        check[cloth] += 1
    for cloth in lost:
        check[cloth] -= 1

    for i in range(1, n+1):
        if not check[i]:
            if check[i-1] > 1:
                check[i-1] -= 1
                check[i] += 1
                
            elif check[i+1] > 1:
                check[i+1] -= 1
                check[i] += 1
    for j in range(1, n+1):
        if check[j]:
            answer += 1

    # answer = sum(check) - 2 - cnt Sum 어딘가에서 문제가생긴거 같은데 어딘지모르겠다.
    return answer

