def solution(s):
    answer = ''
    dic = {
        'zero' : '0', 'one' : '1', 'two' : '2',
        'three' : '3', 'four' : '4', 'five' : '5',
        'six' : '6', 'seven' : '7', 'eight' : '8',
        'nine' : '9'
    }

    t = ''
    for i in s:
        if '0' <= i <= '9':
            answer = answer + i

        else:
            t = t + i
            if t in dic:
                answer = answer + dic[t]
                t = ''

    return int(answer)