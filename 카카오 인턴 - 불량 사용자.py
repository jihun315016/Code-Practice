# 문자열이 제재 아이디일 가능성이 있는지 판단
def check(a, b): # 유저 아이디, 제재 아이디
    for i in range(len(a)):
        if a[i] == '*':
            continue

        if a[i] != b[i]:
            return False

    return True

def solution(user_id, banned_id):
    answer = set()

    # arr[i][j] => i번 제재 아이디에 대해서 가능성있는 유저들 모음
    arr = [[] for _ in range(len(banned_id))]
    visit = [False] * 8

    for i in range(len(banned_id)):
        for j in range(len(user_id)):
            if len(banned_id[i]) == len(user_id[j]):
                if check(banned_id[i], user_id[j]):
                    arr[i].append(str(j))

    s = []
    # 제재 사용자가 될 수 있는 리스트를 answer에 모아주는 역할
    def dfs(index):
        nonlocal answer
        if index == len(arr):
            answer.add(''.join(sorted(s)))
            return

        for i in range(len(arr[index])):
            num = int(arr[index][i])
            if not visit[num]:
                visit[num] = True
                s.append(str(num))
                dfs(index + 1)
                s.pop()
                visit[num] = False

    dfs(0)

    return len(answer)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))