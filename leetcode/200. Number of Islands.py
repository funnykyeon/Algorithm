from typing import List


def numIslands(grid: List[List[str]]) -> int:
    rows, cols = len(grid), len(grid[0])

    cnt = 0
    #섬
    stack = []
    #섬의 좌표
    for row in range(rows):
        for col in range(cols):
            #좌표생성
            if grid[row][col] != '1':
                # 방문한곳이 1인지 아닌지 본다
                continue
            # 아니면 그냥지나감
            cnt += 1
            stack.append((row, col))
            # 1이라면 섬숫자 올리고 좌표 스택으로
            while stack:
                tmp = stack.pop()
                #좌표 스택으로 뺌
                y, x = tmp #
                # 방문한 좌표 스택에서 빼서 표시
                grid[y][x] = '0'
                # 방문한 1은 0으로 변환
                # 1. 북으로 갈 수 있는가?
                if y > 0:
                    # 북쪽 탐색 후 섬이면 스택에 저장
                    if grid[y - 1][x] == '1':
                        stack.append((y - 1, x))
                # 2. 서로 갈 수 있는가?
                if x > 0:
                    # 서쪽 탐색 후 섬이면 스택에 저장
                    if grid[y][x - 1] == '1':
                        stack.append((y, x - 1))
                # 3. 남으로 갈 수 있는가?
                if y < rows - 1:
                    # 서쪽 탐색 후 섬이면 스택에 저장
                    if grid[y + 1][x] == '1':
                        stack.append((y + 1, x))
                # 4. 동으로 갈 수 있는가?
                if x < cols - 1:
                    # 서쪽 탐색 후 섬이면 스택에 저장
                    if grid[y][x + 1] == '1':
                        stack.append((y, x + 1))
            return cnt
        # 단, stack은 역순으로 출력(pop)이 이루어지므로 실질적인 탐색순서는 동 -> 남 -> 서 -> 북이 됨



numIslands(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
])