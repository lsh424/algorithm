def solution(s):
    answer = 0

    def sol(idx1, idx2, s):
        count = 0
        while 0 <= idx1 and idx2 <= len(s) and s[idx1] == s[idx2 - 1]:
            count = max(count, idx2 - idx1)
            idx1 -= 1
            idx2 += 1
        return count

    for i in range(len(s)):
        answer = max(answer, sol(i, i + 1, s), sol(i, i + 2, s))

    return answer