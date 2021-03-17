def solution(record):
    dic = {}
    answer = []

    for i in record:
        lis = i.split(' ')
        if lis[0] == 'Enter' or lis[0] == 'Change':
            dic[lis[1]] = lis[2]

    for rc in record:
        lis = rc.split(' ')

        if lis[0] == 'Enter':
            answer.append(dic[lis[1]] + '님이' + ' 들어왔습니다.')
        elif lis[0] == 'Leave':
            answer.append(dic[lis[1]] + '님이' + ' 나갔습니다.')

    return answer