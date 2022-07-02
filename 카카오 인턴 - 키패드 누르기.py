# 왼손 자표, 오른손 좌표, 도착지 좌표, 무슨 손잡이
def distance(iLeft, jLeft, iRight, jRight, iDes, jDes, hand):
    dLeft = abs(iLeft - iDes) + abs(jLeft - jDes)
    dRight = abs(iRight - iDes) + abs(jRight - jDes)
    if dLeft > dRight:
        return 'R'

    elif dRight > dLeft:
        return 'L'

    else:

        if hand == 'right':
            return 'R'
        else:
            return 'L'


def solution(numbers, hand):
    answer = ''

    numberPos = {
        1 : (0, 0), 2 : (0, 1),
        3 : (0, 2), 4 : (1, 0),
        5 : (1, 1), 6 : (1, 2),
        7 : (2, 0), 8 : (2, 1),
        9 : (2, 2), 0 : (3, 1)
    }

    lPos = (3, 0)
    rPos = (3, 2)

    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            answer = answer + 'L'
            lPos = numberPos[n]

        elif n == 3 or n == 6 or n == 9:
            answer = answer + 'R'
            rPos = numberPos[n]

        else:
            move = distance(
                lPos[0], lPos[1],
                rPos[0], rPos[1],
                numberPos[n][0], numberPos[n][1],
                hand
            )

            answer = answer + move
            if move == 'R':
                rPos = numberPos[n]

            else:
                lPos = numberPos[n]

    return answer
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
