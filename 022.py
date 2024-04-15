class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        s = "()"
        if n == 1:
            return list({s})

        res = set()
        for i in self.generateParenthesis(n-1):
            for j in range(len(i) + 2):
                res.add(i[0:j] + "()" + i[j:])
        return list(res)

print(Solution().generateParenthesis(3))

