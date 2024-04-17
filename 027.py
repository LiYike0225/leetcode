class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if not nums: return 0
        a = b = 0
        while a < len(nums):
            if nums[a] != val:
                nums[b] = nums[a]
                b += 1
            a += 1
        nums = nums[:b]
        return len(nums)

