class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        res = []
        for a, value in enumerate(nums):
            if a > 0 and nums[a-1] == value:
                continue
            num = nums[a]
            left, right = a+1, len(nums)-1
