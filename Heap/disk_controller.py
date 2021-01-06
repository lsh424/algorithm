def solution(jobs):
    total_time = 0
    n = len(jobs)
    end = 0
    jobs.sort(key=lambda x: x[1])

    while jobs:
        for i in range(len(jobs)):
            if jobs[i][0] <= end:
                total_time += (end - jobs[i][0] + jobs[i][1])
                end += jobs[i][1]
                jobs.remove(jobs[i])
                break

            if i == len(jobs) - 1:
                end += 1

    return total_time // n