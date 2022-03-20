from collections import deque
n = int(input())
m = int(input())

graph = []
# 빈 그래프 만든다
visited = [0 for i in range(m)]

#방문기록?
for _ in range(m):
    tmp = list(map(int, input().split()))
    # 쌍 하나씩 불러와서
    graph.append(tmp) # 쌍으로 이루어진 컴퓨터 가져와서 그래프구성
#     그래프에저장!!

# visited를 for문으로 m만큼의 빈칸을 만들어주고
# tmp를 for문으로 m만큼의 연결된 값 가져와서
# graph.append(tmp) => graph에 tmp를 저장
# 4,7 까지 끝나면 아래 덱으로 시작

# 1부터 실행한다.
queue = deque([1])
infection = []
# 빈 감염저장소
while len(queue) != 0:
    # queue길이 가 0과 같지않으면
    target = queue.popleft()
    # 덱에 1을 넣고 시작이니 처음엔 타겟 1 먹고시작
    infection.append(target)#(popleft)한 감염된 데이터 infection으로 넣어줌(1포함)
    tmp = []
    # 스택만들어주고                                       ##처음엔 아무것도없으니 일단for문으로 이동
    for i in range(len(visited)):###############################################################
        # 7열 6개
        if visited[i] == 0: #visited가 0인건 아직 안들른거다
            if graph[i][0] == target:
                print(graph[i][0])
                tmp.append(graph[i][1])
                visited[i] = 1
            elif graph[i][1] == target:
                tmp.append(graph[i][0])
                visited[i] = 1
    #tmp가 queue에 속하지 않고 infection에 속하지 않으면
    for i in tmp:
        if i not in queue:
            queue.append(i) ######################################################################
# print(len(infection)-1)