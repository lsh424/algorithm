def solution(play_time, adv_time, logs):
    def time_to_sec(str):
        components = list(map(int, str.split(":")))
        return components[0] * 3600 + components[1] * 60 + components[2]

    def change_log(str):
        start, end = str.split("-")
        start_sec = time_to_sec(start)
        end_sec = time_to_sec(end)
        return (start_sec, end_sec)

    def sec_to_time(sec):
        h, r = divmod(sec, 3600)
        m, s = divmod(r, 60)
        return str(h).zfill(2) + ':' + str(m).zfill(2) + ':' + str(s).zfill(2)

    play_time_sec = time_to_sec(play_time)
    adv_time_sec = time_to_sec(adv_time)
    total_time = [0 for _ in range(play_time_sec + 1)]

    for log in logs:
        start, end = change_log(log)
        total_time[start] += 1
        total_time[end] -= 1

    for i in range(1, play_time_sec):
        total_time[i] = total_time[i] + total_time[i - 1]

    for i in range(1, play_time_sec):
        total_time[i] = total_time[i] + total_time[i - 1]

    max_time = 0
    answer_sec = 0

    for i in range(adv_time_sec - 1, play_time_sec):
        if max_time < total_time[i] - total_time[i - adv_time_sec]:
            max_time = total_time[i] - total_time[i - adv_time_sec]
            answer_sec = i - adv_time_sec + 1

    return sec_to_time(answer_sec)