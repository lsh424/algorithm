def solution(triangle):
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            if i != 0:
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] = max(triangle[i][j] + triangle[i - 1][j - 1], triangle[i][j] + triangle[i - 1][j])

    return max(triangle[-1])