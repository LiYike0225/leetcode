class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow, fast = 1, 1
        if not nums:
            return 0
        n = len(nums)
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow