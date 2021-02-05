class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        length = len(s)

        def is_available(s: str):
            if not s.isdigit():
                return False

            if len(s) > 1 and s[0] == '0':
                return False

            return 0 <= int(s) <= 255

        def make_ip_add(num: str, s: str, ip: str, count: int):
            ls = []

            if is_available(num):
                if ip.count('.') == 3:
                    ip += num
                else:
                    ip += num
                    ip += '.'
                count += 1

            if count == 4:
                if len(ip) - 3 == length:
                    ls.append(ip)
                    return ls
                else:
                    return ls

            if len(s) > 0:
                ls.extend(make_ip_add(s[0], s[1:], ip, count))

            if len(s) > 1:
                ls.extend(make_ip_add(s[:2], s[2:], ip, count))

            if len(s) > 2:
                ls.extend(make_ip_add(s[:3], s[3:], ip, count))

            return ls

        return make_ip_add('', s, '', 0)
    