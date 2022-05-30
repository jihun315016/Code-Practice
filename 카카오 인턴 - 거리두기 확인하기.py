from collections import deque

def solution(places):
    answer = []

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    def bfs(i, j, arr):
        dq = deque()
        dq.append((i, j, 0))  # i, j, 거리
        visit = [[False] * 5 for _ in range(5)]

        while dq:
            i, j, d = dq.pop()
            visit[i][j] = True

            # 만약 거리가 2가 넘으면 굳이 더 검사할 필요 없음
            if d > 2:
                continue

            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < 5 and 0 <= nj < 5:
                    # 이미 방문한 곳이면 continue
                    if visit[ni][nj]:
                        continue

                    # 파티션이 있는 곳도 continue
                    if arr[ni][nj] == 'X':
                        continue

                    # 거리가 2 이하인데 사람이 있으면 끝
                    # ni, nj는 1칸 이동한 상태니까 d가 아니라 d + 1이어야 한다.
                    if d + 1 <= 2 and arr[ni][nj] == 'P':
                        return False

                    dq.append((ni, nj, d + 1))

        return True

    def func(arr):
        for i in range(5):
            for j in range(5):
                if arr[i][j] == 'P':
                    if not bfs(i, j, arr):
                        return False

        return True

    for arr in places:
        if func(arr):
            answer.append(1)
        else:
            answer.append(0)

    return answer


print(solution(
    [
        ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
        ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
    ]
))