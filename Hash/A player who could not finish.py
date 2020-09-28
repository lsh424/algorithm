import collections

def solution(participant, completion):
    completion_dict = collections.defaultdict(int)

    for completion_person in completion:
        completion_dict[completion_person] += 1

    for i in participant:
        if completion_dict[i] == 0:
            return i
        completion_dict[i] -= 1
        