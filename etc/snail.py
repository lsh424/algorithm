def solution(n):
    answer = []
    length = 0
    top = 0; bottom = n - 1
    row = 0; index = 0
    state = 'down'

    for i in range(1, n + 1):
        length += i
        answer.append([0] * i)

    for i in range(1, length + 1):
        if state == 'down':
            if row < bottom:
                answer[row][index] = i
                row += 1
            elif row == bottom:
                if answer[row][index] == 0:
                    answer[row][index] = i

                if index + 1 > bottom or answer[row][index + 1] != 0:
                    state = 'up'
                    bottom -= 1
                else:
                    index += 1
        else:
            if row - 1 > top:
                row -= 1
                index -= 1
                answer[row][index] = i

                if 0 not in answer[row]:
                    state = 'down'
                    top = row
                    row += 1

    return sum(answer, [])