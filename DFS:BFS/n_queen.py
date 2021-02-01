def find_available_arr(arr: list, row: int, n: int):
    count = 0

    if row == n:
        return 1

    for i in range(n):
        arr[row] = i

        for j in range(row - 1, -1, -1):
            if i == arr[j]:
                break

            if arr[j] > 0 and i == arr[j] - (row - 1 - j) - 1:
                break

            if i > 0 and i - 1 == arr[j] + (row - 1 - j):
                break
        else:
            count += find_available_arr(arr, row + 1, n)

    return count

def solution(n):
    answer = 0
    list = [0] * n
    return find_available_arr(list, 0, n)