import re
import itertools
from collections import deque

def solution(expression):
    ls = []
    p1 = re.compile("\\d+")
    p2 = re.compile("\\D+")

    nums = deque(list(map(lambda x: int(x), p1.findall(expression))))
    ops = deque(p2.findall(expression))
    permutation = list(itertools.permutations(set(ops)))
    exp = []
    
    while nums:
        exp.append(nums.popleft())
        if ops:
            exp.append(ops.popleft())

    def cal(exp, op):
        exp = deque(exp)
        stack = []
        operand = ''

        while exp:
            pop = exp.popleft()

            if type(pop) == int:
                stack.append(pop)
                if exp:
                    operand = exp.popleft()
            else:
                operand = pop

            if exp and op == operand:
                n1 = stack.pop()
                n2 = exp.popleft()
                if op == '*':
                    stack.append(n1 * n2)
                elif op == "+":
                    stack.append(n1 + n2)
                else:
                    stack.append(n1 - n2)
            else:
                stack.append(operand)
        return stack

    for p in permutation:
        e = exp[:]
        for i in p:
            e = cal(e, i)
        ls.append(abs(e[0]))

    return max(ls)