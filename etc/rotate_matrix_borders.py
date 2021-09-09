def solution(rows, columns, queries):
    matrix = [[i + (j * columns) for i in range(1, columns + 1)] for j in range(rows)]
    answer = []

    for query in queries:
        row1, col1, row2, col2 = query
        row1 -= 1
        col1 -= 1
        row2 -= 1
        col2 -= 1

        current = matrix[row1][col1]
        minimum = matrix[row1][col1]
        for c in range(col1 + 1, col2 + 1):
            matrix[row1][c], current = current, matrix[row1][c]
            minimum = min(minimum, current)
        for r in range(row1 + 1, row2 + 1):
            matrix[r][col2], current = current, matrix[r][col2]
            minimum = min(minimum, current)
        for c in range(col2 - 1, col1 - 1, -1):
            matrix[row2][c], current = current, matrix[row2][c]
            minimum = min(minimum, current)
        for r in range(row2 - 1, row1 - 1, -1):
            matrix[r][col1], current = current, matrix[r][col1]
            minimum = min(minimum, current)

        answer.append(minimum)

    return answer