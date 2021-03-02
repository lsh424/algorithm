import itertools

def solution(numbers):
    nums = []
    ls = []
    s = set()
    answer = 0

    for c in numbers:
        nums.append(c)

    for i in range(len(nums)):
        ls.extend(list(itertools.permutations(nums, i + 1)))

    for i in ls:
        num_str = ''.join(i)
        s.add(int(num_str))

    if 0 in s:
        s.remove(0)

    if 1 in s:
        s.remove(1)

    def is_prime(num):
        for i in range(3, num, 2):
            if num % i == 0 or num % 2 == 0:
                if num == i or num == 2:
                    return True
                else:
                    return False
        return True

    for i in s:
        if is_prime(i):
            answer += 1

    return answer