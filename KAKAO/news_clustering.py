def solution(str1, str2):
    A = set()
    B = set()

    def divde_str(str_in):
        st = set()
        dic = dict()
        txt = ''

        for i in range(0, len(str_in) - 1):
            if str_in[i].isalpha() and str_in[i + 1].isalpha():
                txt = str_in[i].lower() + str_in[i + 1].lower()

                if txt in st:
                    if txt in dic:
                        dic[txt] += 1
                    else:
                        dic[txt] = 0

                    st.add(txt + str(dic[txt]))
                else:
                    st.add(txt)
            txt = ''
        return st

    A = divde_str(str1)
    B = divde_str(str2)

    if len((A & B)) == 0 and len((A | B)) == 0:
        J = 1
    else:
        J = len((A & B)) / len((A | B))

    answer = int(J * 65536)

    return answer