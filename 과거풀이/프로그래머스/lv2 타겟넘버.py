# dfs, bfs 타겟넘버구하기.

def solution(numbers, target):
    answer = 0
    
    def dfs(depth, n):
        
        if depth == len(numbers):
            if target == n:
                nonlocal answer
                answer += 1
        else:
            dfs(depth+1, n + numbers[depth])
            dfs(depth+1, n - numbers[depth])
    dfs(0, 0)
    return answer