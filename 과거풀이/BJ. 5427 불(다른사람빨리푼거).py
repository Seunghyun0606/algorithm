# 이사람은 불이 난곳을 visit에 1로 저장하고 아닌곳은 0으로 저장한다음에 풀었음.
# 그래서 만약 z=1 즉 불이난 Q를 뽑은거면 그냥 넘어가고 아니면 visit에서 늘려준 time을 뽑아냄.
# 중요한 포인트는 z 를 통해 1과 0을 사람의 위치, 불의 위치라는 것을 표시후 하나의 단계로 풀었음.
# 나같은 경우는 불지르는 bfs를 한번더 돌아서 3900ms 나오는 반면 이사람은 2700ms 나옴.


from collections import deque
def bfs():
    Q.append((px,py,0))
    visit[px][py]=1
    while Q:
        x,y,z=Q.popleft()
        for i in range(4):
            tx=x+dx[i]
            ty=y+dy[i]
            if tx<0 or tx>=h or ty<0 or ty>=w:
                if z==1:continue
                return visit[x][y]
            if visit[tx][ty] or building[tx][ty]=='#':continue
            visit[tx][ty]=visit[x][y]+1
            Q.append((tx,ty,z))
    return 'IMPOSSIBLE'
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for T in range(int(input())):
    w,h=map(int,input().split())
    building=[list(input()) for _ in range(h)]
    visit=[[0]*w for _ in range(h)]
    Q=deque()
    px=py=0
    for i in range(h):
        for j in range(w):
            if building[i][j]=='*':
                Q.append((i,j,1))
                visit[i][j]=1
            elif building[i][j]=='@':
                px,py=i,j
                building[i][j]='.'
    print(bfs())


# 방법2. 이사람은 그냥 deque를 안쓰고 손수 조건들을 다 써준뒤에, now를 바꾸는 방식을 썼다.
# 왜인지모르겠는데 항상 이렇게 직접써서 하는게 for돌리는거보다 빠르더라.
# 아마 덱에서 pop하는 과정이 없어서 더 빨랐을 가능성이 높다.
# 왜냐면 불필요한 작업들은 안한거나 마찬가지이기 때문.

def BFS(now,fire):
    cnt=0
    while now:
        new_fire=[]
        new_now=[]
        cnt+=1
        for k in fire:
            i,j=k
            if i<h-1 and building[i+1][j]=='.':building[i+1][j]='*';new_fire.append((i+1,j))
            if i>0 and building[i-1][j]=='.':building[i-1][j]='*';new_fire.append((i-1,j))
            if j<w-1 and building[i][j+1]=='.':building[i][j+1]='*';new_fire.append((i,j+1))
            if j>0 and building[i][j-1]=='.':building[i][j-1]='*';new_fire.append((i,j-1))
        for k in now:
            i,j=k
            if i==0 or j==0 or i==h-1 or j==w-1:print(cnt);return
            if i<h-1 and building[i+1][j]=='.':building[i+1][j]='@';new_now.append((i+1,j))
            if i>0 and building[i-1][j]=='.':building[i-1][j]='@';new_now.append((i-1,j))
            if j<w-1 and building[i][j+1]=='.':building[i][j+1]='@';new_now.append((i,j+1))
            if j>0 and building[i][j-1]=='.':building[i][j-1]='@';new_now.append((i,j-1))
        now=new_now
        fire=new_fire
    print('IMPOSSIBLE')
for _ in range(int(input())):
    w,h=map(int,input().split())
    building=[]
    now=[]
    fire=[]
    for i in range(h):
        building.append([*input()])
        for j in range(w):
            if building[i][j]=='@':now.append([i,j])
            elif building[i][j]=='*':fire.append([i,j])
    BFS(now,fire)