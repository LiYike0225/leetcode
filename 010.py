class Solution:
    def maxArea(self, Height: list[int]) -> int:
        left, right, res = 0, len(Height) - 1, 0
        while left < right:
            length = right - left
            height = min(Height[left], Height[right])
            res = max(res, length * height)
            if Height[left] < Height[right]:
                left += 1
            else:
                right -= 1
        return res

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))