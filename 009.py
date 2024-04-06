class Solution:
    def ispalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]

print(Solution().ispalindrome(-121))