from datetime import datetime

def solution(m, musicinfos):
    dic = {'C#': '1','D#' : '2', 'F#' : '3', "G#" : '4', "A#" : '5', 'E#' : '6'}
    answer = []
    i = 0

    def change_note(m):
        s = ''
        for i , n in enumerate(m):
            if n != '#' and i+1 < len(m) and m[i+1] == '#':
                s += dic[n+m[i+1]]
            elif n != '#':
                s += n
        return s

    def music_time(start, end):
        end_t = datetime(2021,1,1,int(end[:2]),int(end[3:]),0)
        start_t =datetime(2021,1,1,int(start[:2]),int(start[3:]),0)
        return int(((end_t - start_t).seconds / 60))

    m = change_note(m)

    for info in musicinfos:
        ls = info.split(",")
        time = music_time(ls[0], ls[1])
        changed_m = change_note(ls[3])
        q, r = divmod(time, len(changed_m))
        s = (changed_m * q) + changed_m[:r]
        if m in s:
            answer.append((ls[2],time,i))
            i += 1

    answer.sort(key = lambda x: (-x[1], x[2]))

    if answer:
        return answer[0][0]
    else:
        return "(None)"