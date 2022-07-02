def solution(board, moves):
    answer = 0
    dolls = []

    # 기계의 깊이는 j이므로
    # i열에 대해 j깊이 만큼 검사한다.
    # 만약 중간에 인형이 뽑히면 break
    for i in moves:
        isDoll = False # 인형을 뽑은 여부
        for j in range(len(board)):
            if board[j][i - 1] != 0:
                dolls.append(board[j][i - 1])
                board[j][i - 1] = 0
                isDoll = True
                break

        if isDoll:
            isPop = True # 인형이 터뜨려지는 여부
            while isPop:
                isPop = False
                for j in range(len(dolls) - 1):
                    if dolls[j] == dolls[j + 1]:
                        dolls.pop(j) # 인형은 둘 다 터뜨릴 것
                        dolls.pop(j)
                        answer = answer + 2
                        isPop = True
                        break

    return answer

print(solution(
    [
        [0,0,0,0,0],
        [0,0,1,0,3],
        [0,2,5,0,1],
        [4,2,4,4,2],
        [3,5,1,3,1]
    ],
    [1,5,3,5,1,2,1,4]
))
