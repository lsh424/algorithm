def solution(s):
    answer = len(s)
    char_len = 1

    while char_len <= len(s) / 2:
        current_word = s[:char_len]
        count = 0
        comp_s = ''
        for i in range(0, len(s), char_len):
            if current_word == s[i:i+char_len]:
                count += 1
            else:
                if count == 1:
                    comp_s += current_word
                else:
                    comp_s += (str(count) + current_word)
                current_word = s[i:i+char_len]
                count = 1

        if count != 0:
            if count == 1:
                comp_s += current_word
            else:
                comp_s += (str(count) + current_word)

        if len(comp_s) < answer:
            answer = len(comp_s)
        char_len += 1

    return answer