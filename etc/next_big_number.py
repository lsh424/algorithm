# O(n)
def solution(n):
    ls = list(bin(n)[2:])

    is_find_one = False
    one_to_zero_idx = len(ls) - 1
    zero_to_one_idx = 0
    for i in range(len(ls) - 1, -1, -1):
        if ls[i] == "1" and is_find_one == False:
            one_to_zero_idx = i
            is_find_one = True

        if is_find_one and ls[i] == "0":
            zero_to_one_idx = i
            break

    ls[one_to_zero_idx] = "0"

    if zero_to_one_idx == 0:
        ls = ["1"] + ls
    else:
        ls[zero_to_one_idx] = "1"

    if ls[zero_to_one_idx + 1:].count("1") > 0:
        change_count = ls[zero_to_one_idx + 1:].count("0")
        one_count = 0
        zero_count = 0
        for i in range(zero_to_one_idx + 1, len(ls)):
            if ls[i] == "1":
                ls[i] = "0"
                one_count += 1

            if one_count == change_count:
                break

        for i in range(len(ls) - 1, zero_to_one_idx, -1):
            if ls[i] == "0":
                ls[i] = "1"
                zero_count += 1

            if zero_count == one_count:
                break

    return (int(''.join(ls), 2))

# O(n^2)
def solution(n):
    num1 = bin(n).count('1')
    while True:
        n = n + 1
        if num1 == bin(n).count('1'):
            break
    return n