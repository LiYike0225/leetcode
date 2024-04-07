class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for index, num in enumerate(nums):
            if index > 0 and num == nums[index-1]:
                continue
            left, right = index+1, len(nums)-1
            while left < right:
                s = num + nums[left] + nums[right]
                if s < 0:
                    left += 1
                elif s>0:
                    right -=1
                else:
                    res.append([num,nums[left],nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return res


print(Solution().threeSum([-1,0,1,2,-1,-4]))
