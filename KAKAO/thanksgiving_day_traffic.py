def solution(lines):
    def change_to_sec(date):
        d = date[11:]
        end_sec = float(d[:2]) * 3600 + float(d[3:5]) * 60 + float(d[6:12])
        start_sec = end_sec - float(d[13:-1]) + 0.001
        return (start_sec, end_sec)

    ls = list(map(change_to_sec, lines))
    answer = 0

    def count_req(start, idx):
        end = round(start + 0.999, 3)
        count = 1

        for i in range(idx + 1, len(ls)):
            if ls[i][0] <= end and ls[i][1] >= start:
                count += 1
        return count

    for i in range(len(ls)):
        answer = max(answer, count_req(ls[i][1], i))

    return answer