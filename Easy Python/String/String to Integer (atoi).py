import re
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        Pattern_atoi = re.compile('(^[-+]?[0-9]+)')
        beg = Pattern_atoi.findall(s)
        # beg = re.findall(r'(^[-+]?[0-9]+)',s)
        # beg = re.findall("^[\+\-]?\d+", s)
        if beg == []:
            return 0
        else:
            # print(type(beg[0]))
            # for x in beg:
            #     print(int(x))
            ret = int(beg[0])
            # print(beg)
        print(ret)

helper = Solution()
helper.myAtoi("657 sdsd")
helper.myAtoi("000043")
helper.myAtoi("-+045")
helper.myAtoi(" 000048 +042 sdsd")
helper.myAtoi("  -049 siernwe 00 ")
helper.myAtoi("siernwe 00 -050  ")