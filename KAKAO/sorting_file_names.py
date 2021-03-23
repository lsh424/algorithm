import re

def solution(files):
    return sorted(files, key = lambda x: (re.findall("[^0-9]+", x)[0].lower(), int(re.findall("\d+", x)[0])))