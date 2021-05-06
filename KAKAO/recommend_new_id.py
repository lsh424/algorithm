import re

def solution(new_id):
    new_id = new_id.lower()
    p = re.compile("[a-z0-9-_.]")
    ls = []
    pre = ''
    for i in p.findall(new_id):
        if not (i == pre == '.'):
            ls.append(i)
            pre = i

    if ls and ls[0] == '.':
        del ls[0]
    if ls and ls[-1] == '.':
        del ls[-1]
    if not ls:
        ls.append('a')

    if len(ls) >= 16:
        ls = ls[:15]
    if ls[-1] == '.':
        del ls[-1]

    if len(ls) <= 2:
        num = 3 - len(ls)
        ls.extend(ls[-1] * num)

    return ''.join(ls)