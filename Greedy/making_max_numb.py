def solution(number, k):
    stack = [number[0]]
    result_len = len(number) - k

    for i in range(1, len(number)):
        if not stack or number[i] <= stack[-1]:
            stack.append(number[i])
        else:
            while stack and number[i] > stack[-1] and k > 0:
                stack.pop()
                k -= 1
            stack.append(number[i])

    return ''.join(stack[:result_len])