from collections import deque


def getPointer(board):
    pointer = [0] * len(board)

    for i in range(len(board)):
        for j in range(len(board)):
            if board[j][i] > 0:
                pointer[i] = j;
                break

    return pointer


def solution(board, moves):
    answer = 0
    dq = deque()

    # 각 지점에서 맨 위의 인형이 있는 위치
    pointer = getPointer(board)

    # 뽑기 시작
    for m in moves:
        # 뽑는 인형의 x, y 좌표
        x = m - 1
        y = pointer[x]

        if x >= len(board) or y >= len(board) or board[y][x] == 0:
            continue

        doll = board[y][x]  # 인형

        board[y][x] = 0
        pointer[x] = pointer[x] + 1

        dq.append(doll)

        # 인형 터트리기 체크
        while True:
            if len(dq) > 1 and dq[-1] == dq[-2]:
                dq.pop()
                dq.pop()
                answer = answer + 2
            else:
                break

    return answer


print(solution(
    [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 3],
        [0, 2, 5, 0, 1],
        [4, 2, 4, 4, 2],
        [3, 5, 1, 3, 1]
    ],
    [1, 5, 3, 5, 1, 2, 1, 4])
)