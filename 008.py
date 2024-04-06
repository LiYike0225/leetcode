class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if s == "":
            return 0
        sign = s[0]
        res =0
        if sign == '-' or sign == '+':
            s = s[1:]

        boundary = -(1<<31) if sign == '-' else (1<<31)-1
        for c in s:
            if c.isdigit():
                res = res*10 + int(c)
            else:
                break
        res = -res if sign == '-' else res
        if res > 2 ** 31 - 1 or res < -2**31:
            return boundary
        else:
            return res



