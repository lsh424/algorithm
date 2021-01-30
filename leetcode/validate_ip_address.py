class Solution:
    def validIPAddress(self, IP: str) -> str:
        def is_valid_IP4(IP):
            nums = IP.split('.')

            if len(nums) != 4:
                return False

            for num in nums:
                if not num.isdecimal():
                    return False

                if num == '' or len(num) > 3:
                    return False
                elif len(num) == 2 and num[0] == '0':
                    return False
                elif len(num) == 3 and num[0] == '0':
                    return False
                elif int(num) > 255 or int(num) < 0:
                    return False

            return True

        def is_valid_IP6(IP):
            nums = IP.split(':')
            available_list = [str(i) for i in range(10)]
            available_list.extend(['a', 'b', 'c', 'd', 'e', 'f'])
            available_list.extend(['A', 'B', 'C', 'D', 'E', 'F'])

            if len(nums) != 8:
                return False

            for num in nums:
                if len(num) > 4 or len(num) < 1:
                    return False

                for i in num:
                    if i not in available_list:
                        return False

            return True

        if is_valid_IP4(IP):
            return 'IPv4'
        elif is_valid_IP6(IP):
            return 'IPv6'
        else:
            return 'Neither'