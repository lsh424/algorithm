def solution(a):
    l = len(a)
    ls = [0] * l
    left_min = float('inf')
    right_min = float('inf')

    for i in range(l):
        if a[i] < left_min:
            ls[i] = 1
            left_min = a[i]
        if a[l - i - 1] < right_min:
            ls[l - i - 1] = 1
            right_min = a[l - i - 1]

    return sum(ls)