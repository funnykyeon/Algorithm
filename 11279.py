import sys
import heapq

input = sys.stdin.readline

max_heap = []

# 연산은 n값만큼 (9)
for _ in range(int(input())):
    x = int(input())

    if x == 0:
        if len(max_heap):
            # 빈배열이 아니라면
            print(heapq.heappop(max_heap)[1])
        #     힙에서 값을 읽어올 때는 각 튜플에서 인덱스 1에 있는 값을 취하면 됨
        #     최대값을 출력후 삭제
        else:
            print(0)
    #       빈배열일때 0을 출력
    else:
        heapq.heappush(max_heap, [-x, x])
#         최대값은(우선 순위, 값) 구조의 튜플(tuple)을 힙에 추가하거나 삭제하면 됨
#         0이아닌 자연수를 받았을때 heappush



# 첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다.
# 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다.
# 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고,
# x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거하는 경우이다.
# 입력되는 자연수는 231보다 작다.
