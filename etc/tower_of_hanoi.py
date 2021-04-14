def solution(n):
    answer = []

    def hanoi(n, f, tmp, t):
        if n == 1:
            answer.append([f, t])
        else:
            hanoi(n - 1, f, t, tmp)
            answer.append([f, t])
            hanoi(n - 1, tmp, f, t)

    hanoi(n, 1, 2, 3)

    return answer