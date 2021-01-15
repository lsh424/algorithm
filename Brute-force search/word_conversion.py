import sys

def solution(begin, target, words):
    def find_min_count(begin, target, words, count):
        answer = sys.maxsize
        begins = []
        new_words = []

        if target not in words:
            return 0

        for word in words:
            n = 0
            for i in range(len(word)):
                if begin[i] != word[i]:
                    n += 1

            if n == 1:
                begins.append(word)
                if word == target:
                    return count + 1
            else:
                new_words.append(word)

        if not begins:
            return sys.maxsize

        for i in begins:
            count = find_min_count(i, target, new_words, count + 1)

            if answer > count:
                answer = count

        if answer == sys.maxsize:
            return 0
        else:
            return answer

    return find_min_count(begin, target, words, 0)